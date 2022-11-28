import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yksi_tuote(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 2)

    def test_kaksi_tuotttae(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.kori.lisaa_tuote(Tuote("kissa", 5))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 7)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        kissa = Tuote("kissa", 3345)
        self.kori.lisaa_tuote(kissa)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(maito in ostokset and maito._saldo == 2, True)

    def test_korista_poisto(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset) == 1 and maito._saldo == 1, True)
        self.kori.poista_tuote(maito)
        ostokset2 = self.kori.ostokset()
        self.assertEqual(len(ostokset2) == 0 and maito._saldo == 0, True)

    def test_korin_tyhjennys(self):
        maito = Tuote("Maito", 3)
        kissa = Tuote("pikku-kissa", 13242)
        koira = Tuote("iso-koira", 134134431343)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kissa)
        self.kori.lisaa_tuote(koira)
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset) == 0 and maito._saldo == 0 and koira._saldo == 0 and
                         kissa._saldo == 0, True)