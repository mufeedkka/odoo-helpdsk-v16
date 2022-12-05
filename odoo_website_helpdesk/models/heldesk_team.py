from odoo import models, fields, api


class HelpDeskTeam(models.Model):
    _name = 'help.team'
    _description = 'Helpdesk Team'

    name = fields.Char('Name')
    team_lead_id = fields.Many2one('res.users', string='Team Leader',
                                   domain=lambda self: [('groups_id', 'in', self.env.ref(
                                       'odoo_website_helpdesk.helpdesk_team_leader').id)])
    member_ids = fields.Many2many('res.users', string='Members', domain=lambda self: [
        ('groups_id', 'in', self.env.ref('odoo_website_helpdesk.helpdesk_user').id)])
    email = fields.Char('Email')
    project_id = fields.Many2one('project.project', string='Project')
    create_task = fields.Boolean(string="Create Task")

    @api.onchange('team_lead_id')
    def members_choose(self):
        fetch_memebers = self.env['res.users'].search([])
        filterd_members = fetch_memebers.filtered(lambda x: x.id != self.team_lead_id.id)
        return {'domain': {'member_ids':
                               [('id', '=', filterd_members.ids), ('groups_id', 'in', self.env.ref('base.group_user').id),
                                ('groups_id', 'not in', self.env.ref('odoo_website_helpdesk.helpdesk_team_leader').id)]}}
