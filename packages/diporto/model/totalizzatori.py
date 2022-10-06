# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('totalizzatori',pkey='id',name_long='totalizzatori',name_plural='totalizzatori',caption_field='id')
        self.sysFields(tbl)
        tbl.column('report_id',size='22',name_long='report id',name_short='report_id').relation('report.id',relation_name='report_totaliz', mode='foreignkey', onDelete='cascade', one_one=True)
        tbl.column('gas1_in',dtype='N',size='8',name_long='gas1 in',name_short='gas1_in')
        tbl.column('gas1_fin',dtype='N',size='8',name_long='gas1 fin',name_short='gas1_fin')
        tbl.column('gas1_vend',dtype='N',size='8',name_long='gas1 vend',name_short='gas1_vend')
        tbl.column('gas2_in',dtype='N',size='8',name_long='gas2 in',name_short='gas2_in')
        tbl.column('gas2_fin',dtype='N',size='8',name_long='gas2 fin',name_short='gas2_fin')
        tbl.column('gas2_vend',dtype='N',size='8',name_long='gas2 vend',name_short='gas2_vend')
        tbl.column('benz_in',dtype='N',size='8',name_long='benz in',name_short='benz_in')
        tbl.column('benz_fin',dtype='N',size='8',name_long='benz fin',name_short='benz_fin')
        tbl.column('benz_vend',dtype='N',size='8',name_long='benz vend',name_short='benz_vend')
    def ricalcolaRimanenze(self,record):
        report_id = record['report_id']
        self.db.deferToCommit(self.db.table('diporto.report').ricalcolaRimanenze,
                                    report_id=report_id,
                                    _deferredId=report_id)
    
    def trigger_onInserted(self,record=None):
        self.ricalcolaRimanenze(record)

    def trigger_onUpdated(self,record=None,old_record=None):
        self.ricalcolaRimanenze(record)

    def trigger_onDeleted(self,record=None):
        if self.currentTrigger.parent:
            return
        self.ricalcolaRimanenze(record) 
