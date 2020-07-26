from datetime import datetime as dt, timedelta as td
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class IxHttpRequestSchedulerWiz(models.TransientModel):
    _name = 'ix.http.request.scheduler.wiz'

    interval_number = fields.Integer(
        default=1,
        help="Repeat every x."
    )
    interval_type = fields.Selection(
        [
            ('minutes', 'Minutes'),
            ('hours', 'Hours'),
            ('days', 'Days'),
            ('weeks', 'Weeks'),
            ('months', 'Months')
        ],
        string='Interval Unit',
        default='months'
    )
    nextcall = fields.Datetime(
        string='First Execution Time',
        required=True,
        default=fields.Datetime.now,
        help="Next planned execution date for this job."
    )

    def activate_wizard(self):
        ctx = self._context
        req_ids = ctx.get('active_ids')

        reqs = self.env['ix.http.request'].with_context(
            nextcall=self.nextcall,
            interval_type=self.interval_type,
            interval_number=self.interval_number
        ).browse(req_ids)
        reqs.activate()

    @api.constrains('nextcall')
    def _validate_nextcall(self):
        for wiz in self:
            gap = dt.now() + td(minutes=3)
            msg = 'First Excution Time must be more than 3 minutes from now!'
            if wiz.nextcall < gap:
                raise ValidationError(_(msg))
