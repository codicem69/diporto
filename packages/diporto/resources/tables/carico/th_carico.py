#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data_car')
        r.fieldcell('doc_nota')
        r.fieldcell('litri_benzina')
        r.fieldcell('litri_gasolio')

    def th_order(self):
        return 'data_car:d'

    def th_query(self):
        return dict(column='id', op='contains', val='',runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('data_car' )
        fb.field('doc_nota' )
        fb.field('litri_benzina' , validate_notnull=True)
        fb.field('litri_gasolio', validate_notnull=True )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
