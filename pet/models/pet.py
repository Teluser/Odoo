from odoo import models, fields, api

class Pet(models.Model):
    _name = "pet"

    name = fields.Char(string="Name", require=True)
    character = fields.Char(string="Character")
    add_info = fields.Text(string="Additional information")
    price = fields.Float(string="Price", require=True)
    