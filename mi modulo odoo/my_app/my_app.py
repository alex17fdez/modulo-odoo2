# -*- coding: utf-8 -*- 
from odoo import models, fields 
class MyTask(models.Model): 
    _name = 'my.task' 
    _description = 'My Task'
    name = fields.Char('Description', required=False) 

    nombreSocio = fields.Char('Nombre Socio', required=False) 
    lugar = fields.Char('Lugar', required=False) 
    dia = fields.Char('Dia', required=False) 
    horaInicio = fields.Char('Hora inicio', required=False) 
    horaFin = fields.Char('Hora fin', required=False) 
    tipoPedido = fields.Char('Tipo de Pedido', required=False) 

    is_done = fields.Boolean('Done?') 
    active = fields.Boolean('Active?', default=True)
    def do_marcar(self):
        self.is_done = not self.is_done
        return True
    def do_limpiar(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
