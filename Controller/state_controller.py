from Controller.modality_controller import ModalityController
from Controller.team_controller import TeamController
from Controller.player_controller import PlayerController
from Controller.game_controller import GameController
from Controller.report_controller import ReportController


class StateController:
    def __init__(self):
        self.__modality_controller = None
        self.__teams_controller = None

    def start_flow(self):
        ModalityController().section_name()
        self.__modality_controller = ModalityController().main()
        TeamController().section_name()
        self.__teams_controller = TeamController()

        number_of_players = self.__modality_controller.modality.number_of_players
        # instantiate first team
        self.__teams_controller.main(number_of_players)
        # instantiate second team
        self.__teams_controller.main(number_of_players)

        GameController(self.__teams_controller).main()
        print(ReportController(self.__modality_controller, self.__teams_controller))
