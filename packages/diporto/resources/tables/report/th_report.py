#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent, page_mixin
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('prezzo_gas')
        r.fieldcell('prezzo_benz')
        r.fieldcell('tot_incasso')
        r.fieldcell('rim_gasolio',background='#e7f6f7')
        r.fieldcell('rim_benzina',background='#defade')

    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='id', op='contains', val='',runOnStart=True)



class Form(BaseComponent):
    #definiamo la form con la parte superiore e una parte inferiore
    def th_form(self, form):
        bc = form.center.borderContainer()
        self.reportTestata(bc.contentPane(region='top',datapath= '.record',height='180px'))
        self.reportDett(bc.contentPane(region='center'))

    def reportTestata(self, bc):
        centro = bc.roundedGroup(title='Dati Report',region='center')
        fb = centro.formbuilder(cols=3, border_spacing='4px')
        fb.field('data',width='7em')
        fb.field('prezzo_gas',width='7em')
        fb.field('prezzo_benz',width='7em')
        fb.div('------------')
        fb.br()
        fb.field('tot_incasso',width='7em')
        fb.br()
        fb.div("------------")
        fb.br()
        fb.field('rim_gasolio',width='7em',readOnly=True)
        fb.field('rim_benzina',width='7em',readOnly=True)
        

    def reportDett(self,pane):
        pane.inlineTableHandler(relation='@report_totaliz',viewResource='ViewFromTotalizzatori',
                            picker='report_id')   
                           
   #    pane = form.record
   #    fb = pane.formbuilder(cols=2, border_spacing='4px')
   #    fb.field('data' )
   #    fb.field('prezzo_gas' )
   #    fb.field('prezzo_benz' )
   #    fb.field('tot_incasso' )
   #    fb.field('rim_gasolio' )
   #    fb.field('rim_benzina' )
   
    def th_bottom_custom(self, bottom):
        bar = bottom.slotBar('10,stampa_report,*,10')
        bar.stampa_report.button('Stampa Report', iconClass='print',
                                    action="""genro.publish("table_script_run",{table:"diporto.report",
                                                                               res_type:'print',
                                                                               resource:'stampa_report',
                                                                               pkey: pkey})""",
                                                                               pkey='=#FORM.pkey') 
    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
