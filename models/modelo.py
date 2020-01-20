from odoo import models, fields, api

class Modelo(models.Model):
    _name = 'calculo.modelo'
    nombre = fields.Char('Articulo', required=True)
    precio = fields.Integer('Precio', required=True)
    iva = fields.Integer('IVA', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    total = fields.Float(string='Total', compute='_total')

    @api.one
    @api.depends('precio', 'cantidad', 'iva')
    def _total(self):
        self.total = self.precio * self.cantidad * (1.+"iva")

