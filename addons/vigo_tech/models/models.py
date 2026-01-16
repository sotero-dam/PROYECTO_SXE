from odoo import models, fields

class ProductoVigo(models.Model):

    # MODELO DONDE ODOO GUARDARÁ LOS PRODUCTOS
    _inherit = 'product.template'

    # CAMPOS TÉCNICOS
    vigo_tipo_componente = fields.Selection([
        ('cpu', 'Procesador'),
        ('gpu', 'Tarjeta Gráfica'),
        ('ram', 'Memoria RAM'),
        ('psu', 'Fuente de Alimentación'),
        ('board', 'Placa Base')
    ], string="Tipo de Componente")

    vigo_modelo_socket = fields.Char(string="Socket / Conector")
    vigo_consumo_w = fields.Integer(string="Consumo (W)")
    vigo_es_gaming = fields.Boolean(string="Producto Gaming", default=True)
    vigo_notas_tecnicas = fields.Text(string="Notas de Montaje")