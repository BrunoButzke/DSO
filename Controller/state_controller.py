from Controller.modality_controller import ModalityController
from Controller.team_controller import TeamController
from Controller.player_controller import PlayerController


class StateController:
    def __init__(self):
        self.__modality_controller = None
        self.__teams_controller = None

    def start_flow(self):
        self.__modality_controller = ModalityController().main()
        self.__teams_controller = TeamController().main(self.__modality_controller.modality.number_of_players)
        self.__teams_controller.main(self.__modality_controller.modality.number_of_players)
