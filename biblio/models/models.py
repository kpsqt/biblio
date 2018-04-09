# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'biblio.book'


    # @api.multi
    # def name_get(self):
    #     res = []
    #     for record in self:
    #         if record.edition:
    #             res.append((record['id'], "%s - Edition %s" % (record.name, record.edition)))
    #         else:
    #             res.append((record['id'], record.name))
    #     return res


    name = fields.Char('Name')
    isbn = fields.Char('ISBN')
    publication_year = fields.Integer('Year of publication')
    description = fields.Text('Description')
    author_id = fields.Many2one('biblio.author','Author')
    category_id = fields.Many2one('biblio.category','Category')
    edition = fields.Integer('Edition')
    image = fields.Binary('Image', attachment=True)


class Category(models.Model):
    _name = 'biblio.category'

    name = fields.Char('Name')
    description = fields.Text('Description')
    book_ids = fields.One2many('biblio.book', 'category_id', 'Books')

class Author(models.Model):
    _name = 'biblio.author'

    name = fields.Char('Name')
    image = fields.Binary('Image', attachment=True)
    birthdate = fields.Date('Date of birth')
    autobiography = fields.Text('Autobiography')
    book_ids = fields.One2many('biblio.book', 'author_id', 'Books')