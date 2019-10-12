from Model.modality import Modality
from View.modality_screen import ModalityScreen

class ModalityController:
    def __init__(self):
        self.__modality = None

    def __str__(self):
        return self.__modality.name

    def create_modality(self, name, number_of_players_per_team, gender):
        self.__modality = Modality(name, number_of_players_per_team, gender)

    def main(self):
        name, players, gender = ModalityScreen().get_data()
        self.create_modality(name, players, gender)
        return self

    @property
    def modality(self):
        return self.__modality
