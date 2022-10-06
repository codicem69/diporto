from gnr.web.gnrbaseclasses import TableScriptToHtml
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method

class Main(TableScriptToHtml):

    maintable = 'diporto.nota_di_consegna'
    #Non indicheremo una row_table ma solo una maintable perché stamperemo i record della selezione corrente
    #virtual_columns = '$notestandard'

    doc_header_height = 60
    doc_footer_height = 50
    grid_header_height = 7
    grid_row_height=6
    grid_style_cell='font-size: 12pt; '

    def defineCustomStyles(self):
        self.body.style(""".cell_label{
                            font-size:10pt;
                            text-align:left;
                            color:gray;
                            text-indent:0mm;}
                            
                            .footer_content{
                            font-size:14pt;
                            font_weight=bold;    
                            text-align:right;
                            margin:10mm;
                            }
                            """)

    def docHeader(self, header):
        layout = header.layout(name='doc_header', margin='2mm',font_size='18pt', border_width=0)
        
        row = layout.row()
        left_cell = row.cell()
       # center_cell = row.cell()
        right_cell = row.cell(width=100)

        self.NotaTestataLeft(left_cell)
       
        self.NotaTestataRight(right_cell)
        
    def NotaTestataLeft(self, c):
        l = c.layout('dati_nota',
                    lbl_class='cell_label',
                    font_size='12pt',
                    border_width=0)
       
        r = l.row(height=10)
        r = l.row(height=10)

        r.cell(self.field('data_nc'), lbl='Data Nota di Consegna',lbl_height=4)
        #r = l.row(height=12)
        r.cell(self.field('protocollo'), lbl='Numero Nota di Consegna',lbl_height=4)
        r = l.row(height=10)
        r.cell(self.field('note'), lbl='Note',lbl_height=4)
        #r = l.row(height=12)
       
            
    def NotaTestataRight(self, c):

        l = c.layout('dati_cliente', border_width=0,
                                     lbl_class='cell_label',
                                     font_size='12pt')
    
        r = l.row(height=10)
        l.row(height=5).cell(lbl='Cliente', font_weight= 'bold')           
        l.row(height=5).cell('Spett.', font_weight= 'bold')
        l.row(height=5).cell(self.field('@cliente_id.rag_sociale'), font_weight= 'bold')
        if len(self.field('@cliente_id.indirizzo')) > 20:
            a=10
        else:
            a=5
        l.row(height=a).cell(self.field('@cliente_id.indirizzo'), font_weight= 'bold') 
       
        l.row(height=5).cell('P.IVA ' + self.field('@cliente_id.p_iva'), font_weight= 'bold', font_size='10pt') 
        l.row(height=5).cell('Cod.Fiscale ' + self.field('@cliente_id.cod_fiscale'), font_weight= 'bold', font_size='10pt')
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
        r.cell('@prod_id.prodotto', name='Prodotto')
        r.cell('quantita', name='Quantità Lt.')
        r.cell('prezzo_un', name='Prezzo Un. Euro')
        r.cell('totale', name='Totale Euro')
        
        #r.cell('prof_id')
        #r.fieldcell('servizi_id',mm_width=0, name='Service')
        #r.fieldcell('descrizione',mm_width=0, name='Description')
        #r.fieldcell('tariffa',mm_width=20, name='Euro',format='#,###.00')

    def gridQueryParameters(self):
        return dict(relation='@dett_nc_id')

    def docFooter(self, footer, lastPage=None):
        l = footer.layout('footer',top=1,left=0.5,
                           lbl_class='caption', 
                           content_class = 'footer_content')
    #    
        r = l.row(height=8)
        r.cell('Totale Euro',content_class='aligned_right', font_size='12pt')
        r.cell(self.field('totale_nc'),width=20,content_class='aligned_right', font_size='12pt')
       
