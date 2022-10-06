#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('rag_sociale')
        r.fieldcell('indirizzo')
        r.fieldcell('p_iva')
        r.fieldcell('cod_fiscale')

    def th_order(self):
        return 'rag_sociale'

    def th_query(self):
        return dict(column='rag_sociale', op='contains', val='',runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('rag_sociale', validate_notnull=True, width='20em')
        fb.field('indirizzo',width='30em' )
        fb.field('p_iva' )
        fb.field('cod_fiscale' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
