# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('prodotti',pkey='id',name_long='prodotti',name_plural='prodotti',caption_field='prodotto',lookup=True)
        self.sysFields(tbl)
        tbl.column('prodotto',name_long='prodotto',name_short='pord')
