# encoding: utf-8
from gnr.core.gnrnumber import floatToDecimal,decimalRound


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('nota_di_consegna',pkey='id',name_long='nota di consegna',name_plural='nota di consegna',caption_field='protocollo')
        self.sysFields(tbl)
        tbl.column('cliente_id',size='22',name_long='cliente id',name_short='cliente_id').relation('cliente.id',relation_name='nc_cliente', mode='foreignkey', onDelete='raise')
        tbl.column('data_nc',dtype='D',name_long='data nc',name_short='data_nc')
        tbl.column('note',name_long='note',name_short='note')
        tbl.column('protocollo',size='14',name_long='protocollo',name_short='prot')
        tbl.column('totale_nc',dtype='N',size='10,2',name_long='totale nc',name_short='totale_nc',format='#,###.00')

    def ricalcolaTotali(self, nc_id=None):
        with self.recordToUpdate(nc_id) as record:
            totale_nc = self.db.table('diporto.dett_nc').readColumns(columns="""SUM($totale) AS totale_nc""",
                                                        where='$nc_id=:n_id', n_id=nc_id)

            record['totale_nc'] = floatToDecimal(totale_nc)
    
    
    def defaultValues(self):
        return dict(data_nc = self.db.workdate)

    def counter_protocollo(self,record=None):
        #F14/000001
        return dict(format='$K$YY/$NNNNNN',code='NC',period='YY',
                    date_field='data_nc',showOnLoad=True,recycle=True)  

    
        