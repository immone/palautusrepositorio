class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
         if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
         else:
            self.m_score2 = self.m_score2 + 1

    def even_game(self):
        values = ["Love-All", "Fifteen-All", "Thirty-All", "Forty-All", "Deuce"]
        return values[min(self.m_score1, 4)]
    
    def non_even_game(self, diff):
        if diff == 1: return "Advantage player1"
        elif diff == -1: return "Advantage player2  "
        elif diff >= 2: return "Win for player1"
        else: return "Win for player2"

    def diffx(self):
        return self.m_score1 - self.m_score2

    def compile_game(self):
        values = ["Love", "Fifteen", "Thirty", "Forty"]
        return values[self.m_score1] + "-" + values[self.m_score2]

    def get_score(self):
        diff = self.diffx()
        if diff == 0: return self.even_game()
        elif self.m_score1 >= 4 or self.m_score2 >= 4: return self.non_even_game(diff)
        else: return self.compile_game()
