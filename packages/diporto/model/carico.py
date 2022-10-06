# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('carico',pkey='id',name_long='carico',name_plural='carico',caption_field='id')
        self.sysFields(tbl)
        tbl.column('data_car',dtype='D',name_long='data carico',name_short='data_car')
        tbl.column('doc_nota',name_long='documento / nota',name_short='doc_nota')
        tbl.column('litri_benzina',dtype='N',size='10,2',name_long='litri benzina',name_short='litri_benzina',format='#,###.00')
        tbl.column('litri_gasolio',dtype='N',size='10,2',name_long='litri gasolio',name_short='litri_gasolio',format='#,###.00')
