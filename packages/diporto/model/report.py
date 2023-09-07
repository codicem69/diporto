# encoding: utf-8
from gnr.core.gnrnumber import floatToDecimal,decimalRound

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('report',pkey='id',name_long='report',name_plural='report',caption_field='data')
        self.sysFields(tbl)
        tbl.column('data',dtype='D',name_long='Data Report',name_short='data')
        tbl.column('prezzo_gas',dtype='N',size='10,3',name_long='Prezzo Gasolio',name_short='prezzo gas',format='#,###.000')
        tbl.column('prezzo_benz',dtype='N',size='10,3',name_long='Prezzo Benzina',name_short='prezzo benz',format='#,###.000')
        tbl.column('contanti',dtype='N',size='10,2',name_short='Contanti',format='#,###.00')
        tbl.column('note_contanti', name_short='Note contanti')
        tbl.column('pos_esterno',dtype='N',size='10,2',name_short='Pos esterno',format='#,###.00')
        tbl.column('note_posest', name_short='Note pos esterno')
        tbl.column('pos_manuale',dtype='N',size='10,2',name_short='Pos manuale',format='#,###.00')
        tbl.column('note_posman', name_short='Note pos manuale')
        tbl.column('somme_np',dtype='N',size='10,2',name_short='Somme non pagate',format='#,###.00')
        tbl.column('note_snp', name_short='Note Somme np')
        tbl.column('tot_incasso',dtype='N',size='10,2',name_long='Totale Incasso',name_short='tot incasso',format='#,###.00')
        tbl.column('tot_gasolio',dtype='N',size='10,2',name_long='Totale Gasolio',name_short='tot incasso',format='#,###.00')
        tbl.column('tot_benzina',dtype='N',size='10,2',name_long='Totale Benzina',name_short='tot incasso',format='#,###.00')
        tbl.column('rim_gasolio',dtype='N',size='10,2',name_long='Rimanenza Gasolio',name_short='rim gasolio',format='#,###.00')
        tbl.column('rim_benzina',dtype='N',size='10,2',name_long='Rimanenza Benzina',name_short='rim benzina',format='#,###.00')
        tbl.column('venduto_gas',dtype='N',size='10,2',name_long='Gasolio vend. Lt',name_short='Gas.vend Lt',format='#,###.00')
        tbl.column('venduto_benz',dtype='N',size='10,2',name_long='Benzina vend. Lt',name_short='Benz.vend. Lt',format='#,###.00')
        tbl.formulaColumn('anno_report',"date_part('year', $data)", dtype='D')
        tbl.formulaColumn('mese_report', """EXTRACT(MONTH FROM $data) || '-' || EXTRACT(YEAR FROM $data)""")

    def ricalcolaRimanenze(self,report_id=None):
        with self.recordToUpdate(report_id) as record:
            gasolio_venduto = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($gas1_vend + $gas2_vend)""",
                                                                    where='$id IS NOT NULL')
            gasolio_vend = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($gas1_vend + $gas2_vend)""",
                                                                    where='$report_id=:r_id', r_id=report_id)
            benzina_venduto = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($benz_vend)""",
                                                                     where='$id IS NOT NULL')
            benzina_vend = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($benz_vend)""",
                                                                     where='$report_id=:r_id',r_id=report_id)
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
                record['venduto_gas'] = floatToDecimal(gasolio_vend)

            if benzina_venduto is None:
                record['rim_benzina'] = None
            if carico_benzina is None:
                record['rim_benzina'] = None   
            else:    
                record['rim_benzina'] = floatToDecimal(carico_benzina - benzina_venduto)
                record['venduto_benz'] = floatToDecimal(benzina_vend)
            