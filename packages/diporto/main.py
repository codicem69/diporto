#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='diporto package',sqlschema='diporto',sqlprefix=True,
                    name_short='Diporto', name_long='diporto', name_full='Diporto')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
