# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError,UserError


class Picking(models.Model):
    """ Inherit stock package to constraint one product by package """
    _inherit = "stock.picking"


    def _get_lines_by_product(self):
        self.ensure_one()
        lines_by_product_dict = {}
        lines_by_product = []
        for line in self.move_lines.filtered(lambda mv:mv.state != 'cancel' and mv.product_uom_qty):
            if lines_by_product_dict.get(line.product_id):
                lines_by_product_dict[line.product_id]['product_uom_qty'] += line.product_uom_qty
                lines_by_product_dict[line.product_id]['quantity_done'] += line.quantity_done
            else:
                lines_by_product_dict.update({line.product_id:{'product_uom_qty':line.product_uom_qty,
                                                          'quantity_done':line.quantity_done,
                                                          'product_uom':line.product_uom}})
        for product,line in lines_by_product_dict.items():
            line.update({'product_id':product})
            lines_by_product.append(line)
        return lines_by_product
