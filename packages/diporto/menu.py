# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        user=self.db.currentEnv.get('user')
        if user != 'admin':
            diporto = root.branch(u"diporto", tags="")
            diporto.thpage(u"carico", table="diporto.carico", tags="")
            diporto.thpage(u"report", table="diporto.report", tags="")
            diporto.thpage(u"nota di consegna", table="diporto.nota_di_consegna", tags="")
            diporto.thpage(u"cliente", table="diporto.cliente", tags="")
            diporto.thpage(u"dett_nc", table="diporto.dett_nc", tags="")
            diporto.thpage(u"totalizzatori", table="diporto.totalizzatori", tags="")
            diporto.lookups(u"Lookup tables", lookup_manager="diporto")
        else:
            diporto = root.branch(u"diporto", tags="")
            diporto.packageBranch('Amministrazione sistema',pkg='adm')
            diporto.packageBranch('System',pkg='sys')
            diporto.thpage(u"carico", table="diporto.carico", tags="")
            diporto.thpage(u"report", table="diporto.report", tags="")
            diporto.thpage(u"nota di consegna", table="diporto.nota_di_consegna", tags="")
            diporto.thpage(u"cliente", table="diporto.cliente", tags="")
            diporto.thpage(u"dett_nc", table="diporto.dett_nc", tags="")
            diporto.thpage(u"totalizzatori", table="diporto.totalizzatori", tags="")
            diporto.lookups(u"Lookup tables", lookup_manager="diporto")
