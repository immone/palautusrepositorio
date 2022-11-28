from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return len(self.ostokset)

    def hinta(self):
        sum = 0
        for e in self.ostokset:
            sum += e._saldo*e._hinta
        return sum
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava in self.ostokset:
            self.ostokset[lisattava].saldo += 1
        else:
            lisattava._saldo = 1
            self.ostokset.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
