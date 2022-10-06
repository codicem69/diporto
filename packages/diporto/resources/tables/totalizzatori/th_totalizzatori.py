#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('report_id')
        r.fieldcell('gas1_in',width='7em')
        r.fieldcell('gas1_fin',width='7em')
        r.fieldcell('gas1_vend',width='7em')
        r.fieldcell('gas2_in',width='7em')
        r.fieldcell('gas2_fin',width='7em')
        r.fieldcell('gas2_vend',width='7em')
        r.fieldcell('benz_in',width='7em')
        r.fieldcell('benz_fin',width='7em')
        r.fieldcell('benz_vend',width='7em')

    def th_order(self):
        return 'report_id'

    def th_query(self):
        return dict(column='id', op='contains', val='')

class ViewFromTotalizzatori(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('report_id')
        r.fieldcell('gas1_in',width='7em',edit=dict(remoteRowController=True, validate_notnull=True))
        r.fieldcell('gas1_fin',width='7em',edit=dict(remoteRowController=True, validate_notnull=True))
        r.fieldcell('gas1_vend',width='7em')
        r.fieldcell('gas2_in',width='7em',edit=dict(remoteRowController=True, validate_notnull=True))
        r.fieldcell('gas2_fin',width='7em',edit=dict(remoteRowController=True, validate_notnull=True))
        r.fieldcell('gas2_vend',width='7em')
        r.fieldcell('benz_in',width='7em',edit=dict(remoteRowController=True, validate_notnull=True))
        r.fieldcell('benz_fin',width='7em',edit=dict(remoteRowController=True, validate_notnull=True))
        r.fieldcell('benz_vend',width='7em')
    
    
    @public_method
    def th_remoteRowController(self,row=None,field=None,**kwargs):

        if row['gas1_in'] and row['gas1_fin']:
            row['gas1_vend'] = int(row['gas1_fin']) - int(row['gas1_in'])
        if row['gas2_in'] and row['gas2_fin']:
            row['gas2_vend'] = int(row['gas2_fin']) - int(row['gas2_in'])
        if row['benz_in'] and row['benz_fin']:
            row['benz_vend'] = int(row['benz_fin']) - int(row['benz_in'])
        return row

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('report_id' )
        fb.field('gas1_in' )
        fb.field('gas1_fin' )
        fb.field('gas1_vend' )
        fb.field('gas2_in' )
        fb.field('gas2_fin' )
        fb.field('gas2_vend' )
        fb.field('benz_in' )
        fb.field('benz_fin' )
        fb.field('benz_vend' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
