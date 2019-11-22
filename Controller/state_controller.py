from Controller.modality_controller import ModalityController
from Controller.team_controller import TeamController
from Controller.player_controller import PlayerController
from Controller.game_controller import GameController
from Controller.report_controller import ReportController

import pickle

class StateController:
    def __init__(self):
        self.__modality_controller = None
        self.__teams_controller = None

    def start_flow(self):
        self.__modality_controller = ModalityController().main()

        arq_modalidade = open('modalidade.pkl', 'wb')
        pickle.dump(self.__modality_controller, arq_modalidade)

        arq_modalidade = open('modalidade.pkl', 'rb')
        print(pickle.load(arq_modalidade)) 

        self.__teams_controller = TeamController()

        number_of_players = self.__modality_controller.modality.number_of_players
        # instantiate first team
        self.__teams_controller.main(number_of_players)
        # instantiate second team
        self.__teams_controller.main(number_of_players)

        GameController(self.__teams_controller).main()
        ReportController(self.__modality_controller, self.__teams_controller).show_report()
