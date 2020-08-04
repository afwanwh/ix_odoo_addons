from odoo import models, fields


class IxHttpTestResultWiz(models.TransientModel):
    _name = 'ix.htpp.test.result.wiz'

    response = fields.Text(
        string='Response'
    )

    def ok(self):
        return True
