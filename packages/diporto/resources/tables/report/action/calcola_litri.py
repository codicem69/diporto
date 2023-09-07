from __future__ import print_function
from gnr.web.batch.btcaction import BaseResourceAction
from decimal import Decimal
from time import sleep
import os

caption = 'Calcola litri venduti' #nome nel menu dei batch
tags = 'admin,user'  #autorizzazione al batch
description =  'Calcola litri venduti' #nome piu completo

class Main(BaseResourceAction):
    batch_prefix = 'agg_litri' #identificatore di batch (univoco)
    batch_title = 'Calcola litri' #titolo all'interno del visore del batch
    batch_delay = 0.5  #periodo campionamento termometro
    batch_steps='main'
    batch_cancellable = True
    #virtual_columns = '$saldo'
    #batch_selection_savedQuery = 'testbatch'

    def step_main(self):
        print('page_id',self.db.currentPage.page_id)
        selection = self.get_selection()#(columns='$id,$doc_n,$importo,$saldo')

        if not selection:
            self.batch_debug_write('Nessun record trovato')
            return
        records = self.get_records(for_update=True) #dalla selezione corrente ottiene un iteratore in formato record
        maximum = len(self.get_selection())
        iteratore_report = self.btc.thermo_wrapper(records,message=self.messaggio_termometro, maximum=maximum)

        #il metodo thermo_wrapper ottiene un iteratore che scorrendo ogni elemento aggiorna il termometro
        nuovo_report=None
        for record in iteratore_report:
            report_id = record['id']
            gasolio_vend = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($gas1_vend + $gas2_vend)""",
                                                                    where='$report_id=:r_id', r_id=report_id)
            benzina_vend = self.db.table('diporto.totalizzatori').readColumns(columns="""SUM($benz_vend)""",
                                                                     where='$report_id=:r_id',r_id=report_id)
            data = record['data']
            prezzogas=record['prezzo_gas']
            prezzobenz=record['prezzo_benz']
            tot_incasso = record['tot_incasso']
            rimgas=record['rim_gasolio']
            rimbenz=record['rim_benzina']

            if tot_incasso > 0:

                nuovo_report = self.db.table('diporto.report').newrecord(id=report_id,data=data,prezzo_gas=prezzogas, prezzo_benz=prezzobenz,contanti=tot_incasso,tot_incasso=tot_incasso,rim_gasolio=rimgas,rim_benzina=rimbenz,venduto_gas=gasolio_vend,venduto_benz=benzina_vend)
                self.db.table('diporto.report').update(nuovo_report)

        if nuovo_report:
            self.db.commit()

    def messaggio_termometro(self,record, curr, tot, **kwargs):
        return "report %s %i/%i" %(record['id'],curr,tot)
