from gnr.web.batch.btcprint import BaseResourcePrint
from gnr.core.gnrstring import slugify
from datetime import datetime
import string
#from gnr.core.gnrlang import GnrException

caption = 'Etichetta Campione'

class Main(BaseResourcePrint):
    batch_title = 'Etichetta campione'
    html_res = 'html_res/etichetta'
    batch_immediate = 'print'
    batch_thermo_lines = 'batch_steps,batch_main,ts_loop'
    #virtual_columns = "@agency_id.fullstyle"
    #templates = 'Ranalli_st'


