class Team:
    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        result = self.players.count(player_name)
        if result:
            return True
        return False
        # return player in self.players
    def play_game(self, game_won):
        if game_won:
            self.points += 3
        




