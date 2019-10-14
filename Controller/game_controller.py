from Controller.abstract_game_controller import AbstractGameController

from View.game_screen import GameScreen


class GameController(AbstractGameController):
    def __init__(self, teams):
        super().__init__()
        self.__teams = teams

    def main(self):
        GameScreen().section_name()
        while True:
            option = GameScreen().get_option()

            if option == 1:
                self.add_score()
            elif option == 2:
                self.add_card()
            elif option == 3:
                self.replace_player()
            elif option == 4:
                break
            else:
                print("\n Opção inválida, tente novamente")

    def add_score(self):
        index_team = GameScreen().get_team(self.__teams.teams)
        score = GameScreen().get_score(self.__teams.teams[index_team].name)
        self.__teams.add_score(index_team, score)

    def add_card(self):
        index_team = GameScreen().get_team(self.__teams.teams)
        index_player = GameScreen().get_player(self.__teams.teams[index_team].players_at_field)
        self.__teams.add_card(index_team, index_player)

    def replace_player(self):
        valid_teams = self.teams_allowed_to_be_replaced(self.__teams.teams)
        index_team = GameScreen().get_team(valid_teams)
        starter, bench = GameScreen().get_replacement_players(
            self.__teams.teams[index_team].players_at_field,
            self.__teams.teams[index_team].players_at_bench
        )
        self.__teams.replace_player(index_team, starter, bench)

    def teams_allowed_to_be_replaced(self, teams):
        valid_teams = []
        for team in teams:
            if(len(team.players_at_field) > 0 and len(team.players_at_bench) > 0):
                valid_teams.append(team)
        return valid_teams