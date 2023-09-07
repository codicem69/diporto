#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa lista report
#
#  Created by Tommaso Cespa on 2023 09


from datetime import datetime
from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Lista Report'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Lista Report'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/lista_report'
    #Questo parametro indica la risorsa di stampa da utilizzare
    templates = 'Carburanti_st'
    #Qui utilizziamo la ns carta intestata

    def table_script_parameters_pane(self, pane,**kwargs):
        #Questo metodo consente l'inserimento di alcuni parametri da utilizzare per la stampa
        current_year = datetime.today().year
        years=''
        for r in range(20):
            years += ',' + (str(current_year-r))
        fb = pane.formbuilder(cols=1, width='220px')
        fb.filteringSelect(value='^.anno', values=years, validate_notnull=True, lbl='!![it]Anno')
        fb.dbselect(value='^.report_id', table='diporto.report', lbl='Report', selected_id='.id', condition='$anno_report=:anno', condition_anno='^.anno', hasDownArrow=True)
