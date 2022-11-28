class Team:
    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = list(players)
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        result = self.players.count(player_name)
        if result:
            return True
        return False

    def play_game(self, team_won):
        if team_won:
            self.points += 3
        




