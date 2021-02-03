#-*- coding: utf-8 -*-
from odoo import models, fields, api
class MyTask(models.Model):
    _name = 'my.task'
    _inherit = ['my.task','mail.thread']
    user_id = fields.Many2one('res.users', 'Responsable')
    date_deadline = fields.Date('Dia de entrega')
    nombreSocio = fields.Char(help="Nombre del socio:")

    lugar = fields.Char(help="Lugar:") 
    dia = fields.Date(help="Dia:") 
    horaInicio = fields.Char(help="Hora inicio reparto") 
    horaFin = fields.Char(help="Hora fin de entrega:") 
    tipoPedido = fields.Char(help="Tipo de Pedido:") 


    def do_marcar(self):
        if self.user_id != self.env.user:
            raise Exception('Solo el responsable ha de marcarla como hecha!')
        else:
            return super(MyTask, self).do_marcar()
    def do_limpiar(self):
        domain = [('is_done', '=', True), '|', ('user_id','=', self.env.uid), ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True