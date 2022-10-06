# encoding: utf-8
from gnr.core.gnrnumber import floatToDecimal,decimalRound

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('report',pkey='id',name_long='report',name_plural='report',caption_field='id')
        self.sysFields(tbl)
        tbl.column('data',dtype='D',name_long='data report',name_short='data_r')
        tbl.column('prezzo_gas',dtype='N',size='10,3',name_long='prezzo gasolio',name_short='prezzo_gas',format='#,###.000')
        tbl.column('prezzo_benz',dtype='N',size='10,3',name_long='prezzo benzina',name_short='prezzo_benz',format='#,###.000')
        tbl.column('tot_incasso',dtype='N',size='10,2',name_long='totale incasso',name_short='tot_incasso',format='#,###.00')
        tbl.column('rim_gasolio',dtype='N',size='10,2',name_long='rimanenza gasolio',name_short='rim_gasolio',format='#,###.00')
        tbl.column('rim_benzina',dtype='N',size='10,2',name_long='rimanenza benzina',name_short='rim_benzina',format='#,###.00')

    def ricalcolaRimanenze(self,report_id=None):
        with self.recordToUpdate(report_id) as record:
            gasolio_venduto = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($gas1_vend + $gas2_vend)""",
                                                                    where='$id IS NOT NULL')

            benzina_venduto = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($benz_vend)""",
                                                                     where='$id IS NOT NULL')

            carico_gasolio = self.db.table('diporto.carico').readColumns(columns="""SUM($litri_gasolio) AS tot_carico_gas""",
                                                            where='$id=$id AND $data_car <= :data_car', 
                                                            data_car=self.db.table('diporto.totalizzatori').readColumns(columns='@report_id.data',
                                                            where='$report_id=:f_id',f_id=report_id))
            
            carico_benzina = self.db.table('diporto.carico').readColumns(columns="""SUM($litri_benzina) AS tot_carico_benz""",
                                                            where='$id=$id AND $data_car <= :data_car', 
                                                            data_car=self.db.table('diporto.totalizzatori').readColumns(columns='@report_id.data',
                                                            where='$report_id=:f_id',f_id=report_id))

            if gasolio_venduto is None:
                record['rim_gasolio'] = None
            if carico_gasolio is None:
                record['rim_gasolio'] = None

            else:    
                record['rim_gasolio'] = floatToDecimal(carico_gasolio - gasolio_venduto)

            if benzina_venduto is None:
                record['rim_benzina'] = None
            if carico_benzina is None:
                record['rim_benzina'] = None   
            else:    
                record['rim_benzina'] = floatToDecimal(carico_benzina - benzina_venduto)

            