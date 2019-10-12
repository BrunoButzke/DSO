from View.player_screen import PlayerScreen
from Model.player import Player

class PlayerController:
    def __init__(self):
        pass

    def create_player(self, registration, number):
        return Player(registration, number)

    def main(self):
        registration, number = PlayerScreen().get_data()
        return self.create_player(registration, number)
