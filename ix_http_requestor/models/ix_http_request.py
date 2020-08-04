from odoo import models, fields, api, _
from odoo.exceptions import UserError
import ast
import json
import requests
import logging
_logger = logging.getLogger(__name__)


class IxHttpRequest(models.Model):
    _name = 'ix.http.request'
    _description = 'HTTP Request'

    name = fields.Char(
        string='Name',
        required=True
    )
    method = fields.Selection(
        [
            ('get', 'GET'),
            ('put', 'PUT'),
            ('post', 'POST'),
            ('delete', 'DELETE')
        ],
        string='HTTP Method',
        default='get',
        required=True
    )
    body = fields.Text(
        string='Body',
        required=True
    )
    header = fields.Text(
        string='Header',
        required=True
    )
    url = fields.Text(
        string='URL',
        required=True
    )
    cron_id = fields.Many2one(
        'ir.cron',
        string='Cron Job'
    )
    cron_active = fields.Boolean(
        string='Scheduled',
        related='cron_id.active'
    )

    @api.model
    def _method_selector(self, url, headers, data):
        method = self.method
        if method == 'get':
            return requests.get(url, data=data, headers=headers)
        elif method == 'post':
            return requests.post(url, data=data, headers=headers)
        elif method == 'delete':
            return requests.delete(url, data=data, headers=headers)
        elif method == 'put':
            return requests.put(url, data=data, headers=headers)
        else:
            return False

    @api.model
    def _request(self):
        res = self._method_selector(
            self.url,
            headers=self._convert_to_dict(self.header),
            data=json.dumps(self._convert_to_dict(self.body))
        )
        return res

    @api.model
    def _convert_to_dict(self, str_to_dict):
        try:
            result = {}
            if str_to_dict:
                result = ast.literal_eval(str_to_dict)
            return result
        except Exception as e:
            _logger.exception(e)
            _error_msg = e.msg + ' line ' + str(e.lineno) + ' offset ' + \
                str(e.offset) + ': ' + e.text
            raise UserError(_(
                'Incorrect format!\n' + _error_msg
            ))

    def test_request(self):
        context = dict(self._context)
        for req in self:
            res = req._request()
            msg_code = 'STATUS CODE: ' + str(res.status_code)
            msg_reason = 'REASON: ' + res.reason
            msg_text = 'RESPONSE: ' + res.text
            msg = msg_code + '\n' + msg_reason + '\n' + msg_text
            context['default_response'] = msg
            return {
                'type': 'ir.actions.act_window',
                'name': _('HTTP Response'),
                'view_mode': 'form',
                'res_model': 'ix.htpp.test.result.wiz',
                'target': 'new',
                'context': context
            }

    def request(self, req_id):
        req = self.browse(req_id)
        return req._request()

    def open_activate_wizard(self):
        for item in self:
            res = {
                'type': 'ir.actions.act_window',
                'name': _('Schedule Request'),
                'view_mode': 'form',
                'res_model': 'ix.http.request.scheduler.wiz',
                'target': 'new',
            }
            return res

    def open_deactivate_wizard(self):
        for item in self:
            res = {
                'type': 'ir.actions.act_window',
                'name': _('Deactivate Scheduler'),
                'view_mode': 'form',
                'res_model': 'ix.http.request.deactivate.wiz',
                'target': 'new',
            }
            return res

    def activate(self):
        ctx = self._context
        nextcall = ctx.get('nextcall')
        interval_type = ctx.get('interval_type')
        interval_number = ctx.get('interval_number')
        for req in self:
            if req.cron_id:
                req.cron_id.active = True
                req.cron_id.nextcall = nextcall
                req.cron_id.interval_type = interval_type
                req.cron_id.interval_number = interval_number
                req.cron_id.name = 'Cron - ' + req.name
            else:
                values = {
                    'user_id': self.env.ref('base.user_root').id,
                    'priority': 1,
                    'interval_number': interval_number,
                    'name': 'Cron - ' + req.name,
                    'model_id': self.env['ir.model']._get(self._name).id,
                    'code': 'model.request(' + str(req.id) + ')',
                    'interval_type': interval_type,
                    'numbercall': -1,
                    'nextcall': nextcall,
                    'active': True,
                }
                cron_id = self.env['ir.cron'].create(values)
                req.cron_id = cron_id

    def deactivate(self):
        for req in self:
            if req.cron_id:
                req.cron_id.active = False
