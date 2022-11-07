import unittest
from statistics import Statistics
from player import Player
from statistics import *

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
         self.reader = PlayerReaderStub()
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
         self.statistics = Statistics(self.reader)
        
    def test_reader(self):
         self.assertEqual(self.statistics.reader, self.reader)
         
    def test_points(self):
         lukija = self.reader.get_players()
         pelaajat = lukija[0]
         self.assertEqual(sort_by_points(pelaajat), 16)
         
    def test_search(self):
         lukija = self.reader.get_players()
         pelaajat = lukija[0]
         self.assertEqual(self.statistics.search("asd"), None)
    
    def test_search2(self):
         lukija = self.statistics._players
         pelaajat = lukija[0]
         self.assertEqual(self.statistics.search("Semenko"), pelaajat)
         
    def test_team(self):
         lukija = self.statistics._players
         pelaajat = lukija[3]
         self.assertEqual(self.statistics.team("DET"), [pelaajat])
         
    def test_top(self):
         lukija = self.statistics._players
         pelaajat = lukija[4]
         self.assertEqual(self.statistics.top(1), [pelaajat, lukija[1]])
         