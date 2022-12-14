from odoo import models,fields
from odoo.exceptions import UserError
class EstateProperty(models.Model):
    _inherit = "estate.property"
    company_id = fields.Many2one('res.company', string="Company", required=True, default=lambda self: self.env.user.company_id)
    invoice_id = fields.Many2one('account.invoice')
    def make_property_sold(self):
        super(EstateProperty, self).make_property_sold()
        journal_id = self.env['account.move'].sudo().with_context(type='out_invoice',default_journal_type='sale')._get_default_journal()
        journal = self.env['account.journal'].sudo().browse(journal_id)
        account_id = journal.default_credit_account_id.id
        if not journal_id:
            raise UserError('Please define an accounting sales journal for the company')
        invoice_lines = [
            {'name': '6% of the selling price', 'quantity': 1, 'price_unit': 0.06*self.selling_price, 'account_id': account_id},
            {'name': 'Administrative fees', 'quantity': 1, 'price_unit': 100.00, 'account_id': account_id}
        ]
        invoice_vals = {
            'partner_id': self.buyer_id.id,
            'user_id': self.salesman_id.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': [(0,0,invoice_line_vals) for invoice_line_vals in invoice_lines],
            'journal_id': journal_id,
        }
        res = self.env['account.invoice'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals)
        self.invoice_id = res
        return res
