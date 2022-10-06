 
from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa NC'

class Main(BaseResourcePrint):
    batch_title = 'Stampa NC'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/StampaNC'
    templates = 'Carburanti_st'

    #Non utilizziamo il table_script_parameters_pane perché ci limiteremo a stampare la selezione corrente
