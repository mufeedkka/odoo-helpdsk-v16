from odoo import models, fields, api


class HelpdeskCategories(models.Model):
    _name = 'helpdesk.categories'
    _description = 'Categories'

    name = fields.Char('Name')
    sequence = fields.Integer('Sequence', default=0)
