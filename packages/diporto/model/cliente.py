# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('cliente',pkey='id',name_long='cliente',name_plural='cliente',caption_field='rag_sociale')
        self.sysFields(tbl)
        tbl.column('rag_sociale',name_long='ragione sociale',name_short='rag_sociale')
        tbl.column('indirizzo',name_long='indirizzo',name_short='indirizzo')
        tbl.column('p_iva',name_long='partita iva',name_short='p_iva')
        tbl.column('cod_fiscale',name_long='codice fisclae',name_short='cod_fiscale')
