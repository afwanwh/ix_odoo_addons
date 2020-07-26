from odoo import models


class IxHttpRequestDeactivateWiz(models.TransientModel):
    _name = 'ix.http.request.deactivate.wiz'

    def deactivate(self):
        ctx = self._context
        req_ids = ctx.get('active_ids')
        reqs = self.env['ix.http.request'].browse(req_ids)
        reqs.deactivate()
