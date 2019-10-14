from Controller.abstract_player_controller import AbstractPlayerController

from View.player_screen import PlayerScreen
from Model.player import Player


class PlayerController(AbstractPlayerController):
    def __init__(self):
        super().__init__()
        pass

    def create_player(self, registration, number):
        return Player(registration, number)

    def main(self):
        registration, number = PlayerScreen().get_data()
        return self.create_player(registration, number)
