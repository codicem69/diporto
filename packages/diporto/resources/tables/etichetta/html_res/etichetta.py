from turtle import width
from gnr.web.gnrbaseclasses import TableScriptToHtml
import datetime


class Main(TableScriptToHtml):
    maintable = 'diporto.etichetta'
    #pdf_service = 'we'
    virtual_columns = """$logo"""
    #Con virtual_columns aggiungo a self.record anche le formulaColumn calcolate che altrimenti di default non verrebbero compilate
    css_requires='etichetta'
    def main(self):
        self.datiDeclaration()
        #Nel metodo main specifichiamo tutti i metodi da eseguire: in questo caso solo un metodo schedaCliente totalmente customizzato

    def datiDeclaration(self):
        self.paperpage = self.getNewPage()
        layout = self.paperpage.layout(
                            um='mm',top=5,left=64,right=64, bottom=3,
                            border_width=0,
                            font_family='Helvetica',
                            font_size='9pt',
                            lbl_height=4,lbl_class='caption',
                            border_color='black')

        logo=self.field('logo')
        layout.row(height=20).cell("""<img src="%s" height="50" align="center"><div style='font-size:8pt;padding:3px;text-align: center'><br><br><br><br><br>PORTO DI ORTONA</div>::HTML""" %logo).layout(name='col1', um='mm', border_color='black', lbl_class='smallCaption',hasBorderTop=True,hasBorderLeft=True,hasBorderRight=True,
                                    vertical_align= 'middle',lbl_height=3, style='line-height:5mm;',content_class='cellheader')


        dati_gd1 = layout.row(height=49,lbl_height=2, lbl_class='smallCaption')
        self.datiGeneral1(dati_gd1)
        dati_gd2 = layout.row(height=30,lbl_height=2, lbl_class='smallCaption')
        self.datiGeneral2(dati_gd2)

        self.paperpage = self.getNewPage()
        layout = self.paperpage.layout(
                            um='mm',top=5,left=64,right=64, bottom=3,
                            border_width=0,
                            font_family='Helvetica',
                            font_size='9pt',
                            lbl_height=4,lbl_class='caption',
                            border_color='black')
        
        logo=self.field('logo')
        layout.row(height=20).cell("""<img src="%s" height="50" align="center"><div style='font-size:8pt;padding:3px;text-align: center'><br><br><br><br><br>PORTO DI ORTONA</div>::HTML""" %logo).layout(name='col1', um='mm', border_color='black', lbl_class='smallCaption',hasBorderTop=True,hasBorderLeft=True,hasBorderRight=True,
                                    vertical_align= 'middle',lbl_height=3, style='line-height:5mm;',content_class='cellheader')
        
        dati_gd1 = layout.row(height=49,lbl_height=2, lbl_class='smallCaption')
        self.datiGeneral1(dati_gd1)
        dati_gd2 = layout.row(height=30,lbl_height=2, lbl_class='smallCaption')
        self.datiGeneral_cte(dati_gd2)

    def datiGeneral1(self, row):

        col1 = row.cell().layout(name='col1', um='mm', border_color='black', lbl_class='smallCaption',hasBorderTop=True,hasBorderLeft=True,
                                    vertical_align= 'middle',lbl_height=3, style='line-height:5mm;font-size:8pt;',content_class='celldata')
        col2 =  row.cell().layout(name='col2', um='mm', border_color='black', lbl_class='smallCaption',hasBorderTop=True,hasBorderLeft=True,
                                    vertical_align= 'middle',lbl_height=3, style='line-height:4mm;font-size:8pt;',content_class='celldata')
        col1.row(height=7).cell('IMBARCAZIONE', lbl='')
        col2.row(height=7).cell(self.field('@imbarcazione_id.nome'), lbl='', font_weight='bold')
        col1.row(height=7).cell('PRODOTTO', lbl='')
        col2.row(height=7).cell(self.field('@prodotto_id.prodotto'), lbl='', font_weight='bold')
        col1.row(height=7).cell('Densità ambiente', lbl='')
        col2.row(height=7).cell(self.field('dens_amb'), lbl='', font_weight='bold')
        col1.row(height=7).cell('Densità 15°', lbl='')
        col2.row(height=7).cell(self.field('dens_15'), lbl='', font_weight='bold')
        col1.row(height=7).cell("Memorandum d'imbarco n.", lbl='')
        col2.row(height=7).cell(self.field('mem_n'), lbl='', font_weight='bold')
        col1.row(height=7).cell('Data rifornimento', lbl='')
        col2.row(height=7).cell(self.field('data'), lbl='', font_weight='bold')
        col1.row(height=7).cell('Sigillo campione n.', lbl='')
        col2.row(height=7).cell(self.field('sigillo'), lbl='', font_weight='bold')


    def datiGeneral2(self, row):
        col1 = row.cell().layout(name='col1', um='mm', border_color='black', lbl_class='smallCaption',hasBorderTop=True,hasBorderLeft=True,
                                    vertical_align= 'middle',lbl_height=3, style='line-height:4mm;font-size:8pt;',content_class='celldata')
        col1.row(height=30).cell('Ditta Ranalli Giuseppe S.r.l.', font_weight='bold', lbl="")

    def datiGeneral_cte(self, row):
        col1 = row.cell().layout(name='col1', um='mm', border_color='black', lbl_class='smallCaption',hasBorderTop=True,hasBorderLeft=True,
                                    vertical_align= 'middle',lbl_height=3, style='line-height:4mm;font-size:8pt;',content_class='celldata')
        col1.row(height=40).cell('per Ricevuta<br>IL COMANDANTE::HTML', font_weight='bold', lbl="")    
        
    def outputDocName(self, ext=''):
        vessel = self.record['@imbarcazione_id.nome']
        return 'Etichetta_{vessel}.{ext}'.format(vessel=vessel,ext=ext)
        #return 'Nota_arrivo.{ext}'.format(ext=ext)
