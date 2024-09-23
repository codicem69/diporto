class Table(object):
    def config_db(self,pkg):
        
        tbl=pkg.table('logo', pkey='id', name_long='!![it]Logo', name_plural='!![it]Loghi',
                                 caption_field='id')
        self.sysFields(tbl,counter=True)
        tbl.column('logo', dtype='P', name_short='!![it]Logo')