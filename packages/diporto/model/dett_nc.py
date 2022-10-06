# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('dett_nc',pkey='id',name_long='dett_nc',name_plural='dett_nc',caption_field='id')
        self.sysFields(tbl)
        tbl.column('nc_id',size='22',name_long='nc_id',name_short='nc_id').relation('nota_di_consegna.id',relation_name='dett_nc_id', mode='foreignkey', onDelete='cascade')
        tbl.column('prod_id',size='22',name_long='prodotto id',name_short='prod_id').relation('prodotti.id',relation_name='dett_nc_prod_id', mode='foreignkey', onDelete='raise')
        tbl.column('quantita',dtype='N',size='10,2',name_long='quantità',name_short='quantita',format='#,###.00')
        tbl.column('prezzo_un',dtype='N',size='10,3',name_long='prezzo unitario',name_short='prezzo_un',format='#,###.000')
        tbl.column('totale',dtype='N',size='10,2',name_long='totale',name_short='tot',format='#,###.00')

    def ricalcolaTotali(self,record):
            nc_id = record['nc_id']
            self.db.deferToCommit(self.db.table('diporto.nota_di_consegna').ricalcolaTotali,
                                    nc_id=nc_id,
                                    _deferredId=nc_id)
    
    def trigger_onInserted(self,record=None):
        self.ricalcolaTotali(record)

    def trigger_onUpdated(self,record=None,old_record=None):
        self.ricalcolaTotali(record)
        
    def trigger_onDeleted(self,record=None):
        if self.currentTrigger.parent:
            return
        self.ricalcolaTotali(record)