from View.player_screen import PlayerScreen
from Model.player import Player

class PlayerController:
    def __init__(self):
        pass

    def create_player(self, matricula, number):
        return Player(matricula, number)

    def main(self):
        matricula, number = PlayerScreen().get_data()
        return self.create_player(matricula, number)
