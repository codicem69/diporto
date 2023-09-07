from gnr.web.gnrbaseclasses import TableScriptToHtml
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method

class Main(TableScriptToHtml):

    maintable = 'diporto.report'
    #Non indicheremo una row_table ma solo una maintable perché stamperemo i record della selezione corrente
    #virtual_columns = '$notestandard'

    doc_header_height = 150
    doc_footer_height = 30
    grid_header_height = 7
    grid_row_height=8
    grid_style_cell='font-size: 14pt'
   # grid_style_cell='font-weight:bold; font-size:14pt; font-style:italic; font-family:mono; line-height: 2'            

    def defineCustomStyles(self):
        self.body.style(""".cell_label{
                            font-size:12pt;
                            text-align:center;
                            color:gray;
                            margin:0mm;
                            text-indent:1mm;}
    
                            .footer_content{
                            font-size:24pt;
                            font_weight=bold;    
                            text-align:center;
                            margin:0mm;
                            }
                            """)
        
        
    def docHeader(self, header):
        
        layout = header.layout(name='doc_header', margin='2mm',font_size='12pt', border_width=0)
        
        row = layout.row()
        cell = row.cell()
        #center_cell = row.cell()
        #right_cell = row.cell(width=80)

        self.ReportTestata(cell)
        #self.ReportTestataRight(right_cell)
        
    def ReportTestata(self, c):
        l = c.layout('dati_report',
                   lbl_class='cell_label',
                   font_size='16pt',
                   border_width=1)
        
     
        r = l.row(height=12)
        r = l.row(height=12,row_border=False)

        r.cell(self.field('data'), lbl='Data Report',content_class='aligned_center',lbl_height=5)
        #r = l.row(height=12)
        r.cell(self.field('prezzo_gas'), lbl='Prezzo Gasolio',content_class='aligned_center',lbl_height=5)
        #r = l.row(height=12)
        r.cell(self.field('prezzo_benz'), lbl='Prezzo Benzina',content_class='aligned_center',lbl_height=5)
        r = l.row(height=12,row_border=False)
        r = l.row(font_size='12pt')
        r.cell(self.field('contanti'),lbl='Contanti',content_class='aligned_center',lbl_height=5, width=50)
        r.cell(self.field('note_contanti'),lbl='Note contanti',content_class='aligned_center',lbl_height=5)
        r = l.row(font_size='12pt')
        r.cell(self.field('pos_esterno'),lbl='Pos Esterno',content_class='aligned_center',lbl_height=5, width=50)
        r.cell(self.field('note_posest'),lbl='Note Pos esterno',content_class='aligned_center',lbl_height=5)
        r = l.row(font_size='12pt')
        r.cell(self.field('pos_manuale'),lbl='Pos Manuale',content_class='aligned_center',lbl_height=5, width=50)
        r.cell(self.field('note_posman'),lbl='Note Pos manuale',content_class='aligned_center',lbl_height=5)
        r = l.row(font_size='12pt')
        r.cell(self.field('somme_np'),lbl='Somme non pagate',content_class='aligned_center',lbl_height=5, width=50)
        r.cell(self.field('note_snp'),lbl='Note somme non pagate',content_class='aligned_center',lbl_height=5)
        r = l.row(height=12, font_weight='bold')
        r.cell(self.field('tot_incasso'), lbl='Totale Incasso',content_class='aligned_center',lbl_height=5)
        r = l.row(height=12)
     
       
        
    #def ReportTestataRight(self, c):
     #   l = c.layout('dati_cliente', border_width=0)
        
       ##l.row(height=5).cell('Messrs.', font_weight= 'bold')
       #l.cell(self.field('tot_incasso'), lbl='Totale Incasso')
       #l = l.row(height=8)
       #l.cell(self.field('rim_gasolio'), lbl='Rimanenza Gasolio')
       #l = l.row(height=8)
       #l.cell(self.field('rim_benzina'), lbl='Rimanenza Benzina')
       #l = l.row(height=8)
    
    #def gridData(self):
     #   return dict(relation='@report_totaliz')
        

    def gridStruct(self,struct):
        
        r = struct.view().rows()
        #print(c)
        r.cell('gas1_in', name='Gasolio 1 Iniz.')
        r.cell('gas1_fin', name='Gasolio 1 Finale')
        r.cell('gas1_vend', name='Gasolio 1 Erogato',background='#92b6e1', color='blue',content_class='aligned_center')
        r.cell('gas2_in', name='Gasolio 2 Iniz.')
        r.cell('gas2_fin', name='Gasolio 2 Finale')
        r.cell('gas2_vend', name='Gasolio 2 Erogato',background='#92b6e1',content_class='aligned_center')
        r.cell('benz_in', name='Benzina Iniz.')
        r.cell('benz_fin', name='Benzina Finale')
        r.cell('benz_vend', name='Benzina Erogata',background='#a2f9c3',content_class='aligned_center')
 
        
        #r.cell('prof_id')
        #r.fieldcell('servizi_id',mm_width=0, name='Service')
        #r.fieldcell('descrizione',mm_width=0, name='Description')
        #r.fieldcell('tariffa',mm_width=20, name='Euro',format='#,###.00')

    def gridQueryParameters(self):
        return dict(relation='@report_totaliz')

    def docFooter(self, footer, lastPage=None):
        l = footer.layout('footer',top=1,left=0.5,
                           lbl_class='caption', 
                           content_class = 'footer_content')
    #    
        r = l.row(height=8)
        r.cell('Rimanenza gasolio lt.',content_class='aligned_right', font_size='12pt')
        r.cell(self.field('rim_gasolio'),width=20,content_class='aligned_right', font_size='12pt')
        r = l.row(height=8)
        r.cell('Rimanenza benzina lt.',content_class='aligned_right', font_size='12pt')
        r.cell(self.field('rim_benzina'),width=20,content_class='aligned_right', font_size='12pt')

       #                          
       #r = l.row(height=6)
       #r.cell('Total PFDA Euro',content_class='aligned_right', font_size='12pt', font_weight= 'bold',row_border=False)
      
       #r.cell(self.field('totalepfda'),content_class='aligned_right', width=20, font_weight= 'bold')
       #r = l.row()
      
       #noteproforma = (self.field('noteproforma')) 
       #
       #note_standard = self.db.application.getPreference('notestandard',pkg='pfda')       
       #
   
       #r.cell(str(noteproforma) + str("{note_standard}::HTML".format(note_standard=note_standard)), content_class='aligned_left', font_size='8pt')
        
    
         
   #def calcDocFooterHeight(self):  
   #        if self.record['noteproforma']:
   #        
   #            return self.doc_header_height + 50
   #        else:
   #            return self.doc_footer_height    

        
