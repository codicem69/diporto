 
from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa New Report'

class Main(BaseResourcePrint):
    batch_title = 'Stampa New Report'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/StampaNewReport'
    templates = 'Carburanti_st'

    #Non utilizziamo il table_script_parameters_pane perché ci limiteremo a stampare la selezione corrente
