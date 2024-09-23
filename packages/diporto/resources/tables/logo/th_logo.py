#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('logo')

    def th_order(self):
        return 'logo'

    def th_query(self):
        return dict(column='id', op='contains', val='')


class Form(BaseComponent):

    def th_form(self, form):
        bc= form.center.borderContainer()
        self.loghi(bc.borderContainer(region='top',datapath='.record',height='100%', splitter=True))

    def loghi(self,bc):
        logocp = bc.roundedGroup(title='Logo',width='700px',region='left')
        logocp.img(src='^.logo', edit=True, crop_width='250px', crop_height='50px',
                        placeholder=True, upload_folder='*')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )    
        
#class Form(BaseComponent):
#
#    def th_form(self, form):
#        pane = form.record
#        fb = pane.formbuilder(cols=2, border_spacing='4px')
#        fb.field('logo' )
#
#
#    def th_options(self):
#        return dict(dialog_height='400px', dialog_width='600px' )
