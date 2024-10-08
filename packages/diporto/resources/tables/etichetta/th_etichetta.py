#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.web.gnrbaseclasses import TableTemplateToHtml
from datetime import datetime

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('imbarcazione_id')
        r.fieldcell('prodotto_id')
        r.fieldcell('dens_amb')
        r.fieldcell('dens_15')
        r.fieldcell('mem_n')
        r.fieldcell('data')
        r.fieldcell('sigillo')

    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='@imbarcazione_id.nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('imbarcazione_id', hasDownArrow=True )
        fb.field('prodotto_id' )
        fb.field('dens_amb',format='#,###.000' )
        fb.field('dens_15' ,format='#,###.000')
        fb.field('mem_n' )
        fb.field('data' )
        fb.field('sigillo' )
        #btn = fb.Button('!![it]Stampa etichetta')
        #btn.dataRpc('', self.print_template, record='=#FORM.record',
        #                    nome_template = 'diporto.etichetta:etichetta',format_page='A4',_onCalling="this.form.save();")
        fb.Button('!![it]Stampa etichetta',action="""genro.publish("table_script_run",{table:"diporto.etichetta",
                                                                               res_type:'print',
                                                                               resource:'etichetta',
                                                                               pkey: pkey})
                                                                               this.form.save();""",
                                                                               pkey='=#FORM.pkey')
    @public_method
    def print_template(self, record, resultAttr=None, nome_template=None, format_page=None, **kwargs):
        
        record_id=record['id']
     
        tbl_etichetta = self.db.table('diporto.etichetta')
        builder = TableTemplateToHtml(table=tbl_etichetta)

        nome_temp = nome_template.replace('diporto.etichetta:','')
        nome_file = '{cl_id}.pdf'.format(
                    cl_id=nome_temp)
        
        template = self.loadTemplate(nome_template)  # nome del template
        pdfpath = self.site.storageNode('home:stampe_template', nome_file)

        tbl_htmltemplate = self.db.table('adm.htmltemplate')
        templates= tbl_htmltemplate.query(columns='$id,$name', where='').fetch()
        letterhead=''       
        for r in range(len(templates)):
            if templates[r][1] == 'A4_vert':
                letterhead = templates[r][0]    
            if format_page=='A3':
                if templates[r][1] == 'A3_orizz':
                    letterhead = templates[r][0]
          
        builder(record=record_id, template=template,letterhead_id=letterhead)

        result = builder.writePdf(pdfpath=pdfpath)

        self.setInClientData(path='gnr.clientprint',
                              value=result.url(timestamp=datetime.now()), fired=True)
  

    def th_options(self):
        return dict(dialog_windowRatio = 1)
        #return dict(dialog_height='400px', dialog_width='600px' )
