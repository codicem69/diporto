# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        root.packageBranch('Amministrazione sistema',pkg='adm')
        root.packageBranch('System',pkg='sys')
        root.packageBranch('Contabilità carburanti',pkg='acc_mp')
        diporto = root.branch(u"diporto", tags="")
        diporto.thpage(u"carico", table="diporto.carico", tags="")
        diporto.thpage(u"report", table="diporto.report", tags="")
        diporto.thpage(u"nota di consegna", table="diporto.nota_di_consegna", tags="")
        diporto.thpage(u"cliente", table="diporto.cliente", tags="")
        diporto.thpage(u"dett_nc", table="diporto.dett_nc", tags="")
        diporto.thpage(u"totalizzatori", table="diporto.totalizzatori", tags="")
        diporto.thpage(u"etichette", table="diporto.etichetta", tags="")
        diporto.thpage(u"logo", table="diporto.logo", tags="")
        diporto.lookups(u"Lookup tables", lookup_manager="diporto")


