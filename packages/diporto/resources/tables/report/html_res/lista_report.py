#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa statistiche fatturato
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.

from gnr.web.gnrbaseclasses import TableScriptToHtml

class Main(TableScriptToHtml):
    maintable = 'diporto.report'
    row_table = 'diporto.report'
    page_width = 210
    page_height = 297
    doc_header_height = 30
    doc_footer_height = 8
    grid_header_height = 10
    totalize_footer='Totale incassato'
    #Fornendo a totalize_footer una stringa testuale, questa verrà usata come etichetta della riga di totalizzazione
    empty_row=dict()
    #Grazie a questo parametro in caso di mancanza di dati verrà stampata una griglia vuota invece di una pagina bianca


    def docHeader(self, header):
        #Questo metodo definisce il layout e il contenuto dell'header della stampa
        head = header.layout(name='doc_header', margin='5mm', border_width=0)
        row = head.row()
        row.cell("""<center><div style='font-size:18pt;'><strong>Lista Report per periodo</strong></div>
                    <div style='font-size:14pt;'>Anno {anno}</div></center>::HTML""".format(anno=self.parameter('anno')))
        if self.parameter('report_id'):
            row = head.row()
            row.cell("""<center><div style='font-size:14pt;'>Report del {report}</div></center>::HTML""".format(
                                report=self.rowField('data')))


    def defineCustomStyles(self):
        #Questo metodo definisce gli stili del body dell'html
        self.body.style(""".cell_label{
                            font-size:8pt;
                            text-align:left;
                            color:grey;
                            text-indent:1mm;}

                            .footer_content{
                            text-align:right;
                            margin:2mm;
                            }
                            """)

    def gridStruct(self,struct):
        #Questo metodo definisce la struttura della griglia di stampa definendone colonne e layout
        r = struct.view().rows()
        r.fieldcell('data', mm_width=12)
        #Questa formulaColumn verrà utilizzata per creare i subtotali per mese
        r.fieldcell('prezzo_gas', mm_width=9, name='Prezzo Gas')
        r.fieldcell('prezzo_benz', mm_width=9, name='Prezzo Benz')
        r.fieldcell('contanti', mm_width=0)
        r.fieldcell('pos_esterno', mm_width=0)
        r.fieldcell('pos_manuale', mm_width=0)
        r.fieldcell('somme_np', mm_width=0)
        r.fieldcell('mese_report',  subtotal='Totale mese {breaker_value}', subtotal_order_by="$data", mm_width=0,hidden=True)
        r.fieldcell('tot_incasso', mm_width=0, totalize=True)


        r.fieldcell('venduto_gas', mm_width=12, totalize=True)
        r.fieldcell('venduto_benz', mm_width=12, totalize=True)

    def gridQueryParameters(self):
        #Questo metodo fornisce a gridData i parametri (condizioni, relation, table) sulla base dei quali costruire
        #le righe con i dati da riportare in griglia. In questo caso uso una condizione.
        condition=['$anno_report=:anno']
        if self.parameter('report_id'):
            condition.append('$id=:report')
        return dict(condition=' AND '.join(condition), condition_anno=self.parameter('anno'),
                        condition_report=self.parameter('report_id'))

    def docFooter(self, footer, lastPage=None):
        #Questo metodo definisce il layout e il contenuto dell'header della stampa
        foo = footer.layout('totali_fattura',top=1,
                           lbl_class='cell_label',
                           content_class = 'footer_content')
        r = foo.row()
        r.cell('Documento stampato il {oggi}'.format(oggi=self.db.workdate))

    def outputDocName(self, ext=''):
        #Questo metodo definisce il nome del file di output

        if ext and not ext[0] == '.':
            ext = '.%s' % ext
        if self.parameter('report_id'):

            doc_name = 'Reports_{anno}_{report}{ext}'.format(anno=self.parameter('anno'),
                        report='', ext=ext)
        else:
            doc_name = 'Reports_{anno}{ext}'.format(anno=self.parameter('anno'), ext=ext)
        return doc_name
