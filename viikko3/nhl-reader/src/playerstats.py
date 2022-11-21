from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.stats = reader

    def top_scorers_by_nationality(self, country):
        response = self.stats.response
        players = []
        for player_dict in response:
            team = player_dict['team']
            goals = player_dict['goals']
            assists = player_dict['assists']
            name = player_dict['name']
            goals = player_dict['goals']
            assists = player_dict['assists']
            games = player_dict['games']
            penalties = player_dict['penalties']
            nationality = player_dict['nationality']
            player = Player(
                name, team, goals, assists, nationality, penalties, games
            )
            if nationality == country:
                players.append(player)
        players = sorted(players, key=lambda x: -x.points)
        return players