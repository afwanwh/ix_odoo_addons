from openerp import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ix_code = fields.Char(string='Contact Code')
    ix_show = fields.Boolean(string='Show in Selection Fields')

    _sql_constraints = [('code_uniq', 'UNIQUE(code)', _('Two or more same codes are disallowed. Define another code.'))]

    @api.multi
    def name_get(self):
        res = super(ResPartner, self).name_get()
        new_res = []
        for item in res:
            partner_id = self.browse(item[0])
            name = item[1]
            if partner_id.ix_show and partner_id.ix_code:
                name = '[' + partner_id.ix_code + '] ' + name
            new_res.append((item[0], name))
        return new_res
