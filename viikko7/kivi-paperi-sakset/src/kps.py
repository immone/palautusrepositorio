from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

def tee_peli(inp):
    if inp == 'a':
        game = KPSPelaajaVsPelaaja()
        game.pelaa()
    elif inp == 'b':
        game = KPSTekoaly()
        game.pelaa()
    elif inp == 'c':
        game =  KPSParempiTekoaly()
        game.pelaa()
    else:
        pass

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        pass

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto

class KPSParempiTekoaly(KiviPaperiSakset):

    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)

        return siirto


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)

        return siirto
