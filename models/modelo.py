from odoo import models, fields, api

class Modelo(models.Model):
    _name = 'calculo.modelo'
    nombre = fields.Char('Articulo', required=True)
    precio = fields.Float('Precio', required=True)
    iva = fields.Integer('IVA', required=True)
    desglose = fields.Float(string='Desglose', compute='_iva')
    cantidad = fields.Integer('Cantidad', required=True)
    total = fields.Float(string='Total', compute='_total')
    totalIVA = fields.Float(string='TotalIVA', compute='_sumaTotal')


    @api.one
    @api.depends('precio', 'cantidad')
    def _total(self):
        self.total = self.precio * self.cantidad

    @api.one
    @api.depends('precio', 'cantidad', 'iva')
    def _iva(self):
        self.desglose = self.precio * self.cantidad * ((self.iva/100)+1)
        self.desglose = self.desglose - (self.precio * self.cantidad)

    @api.one
    @api.depends('total', 'desglose')
    def _sumaTotal(self):
        self.totalIVA = self.total + self.desglose

