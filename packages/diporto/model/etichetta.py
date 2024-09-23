# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('etichetta', pkey='id', name_long='!![it]Etichetta campione', name_plural='!![it]Etichette campioni',caption_field='imbarcazione_id')
        self.sysFields(tbl)
        tbl.column('imbarcazione_id', size='22', name_short='!![it]Imbarcazione'
                   ).relation('acc_mp.imbarcazione.id', mode='foreignkey', onDelete='raise', one_one='*')
        tbl.column('prodotto_id',size='22', name_long='!![it]Prodotto'
                    ).relation('prodotti.id', relation_name='prod', mode='foreignkey', onDelete='raise')
        tbl.column('dens_amb', dtype='N', name_short='!![it]Densità ambiente')
        tbl.column('dens_15', dtype='N', name_short='!![it]Densità 15°')
        tbl.column('mem_n', name_short='!![it]Memorandum n.')
        tbl.column('data', dtype='D', name_short='!![it]Data')
        tbl.column('sigillo', name_short='!![it]Sigillo n.')
        tbl.formulaColumn('logo',select=dict(table='diporto.logo', columns="$logo",
                                                    where=''), dtype='P')