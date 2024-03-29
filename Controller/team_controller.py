from Controller.abstract_team_controller import AbstractTeamController

from View.team_screen import TeamScreen
from Model.team import Team
from Controller.player_controller import PlayerController


class TeamController(AbstractTeamController):
    def __init__(self):
        super().__init__()
        self.__teams = []

    @property
    def teams(self):
        return self.__teams

    def add_score(self, index_team, score):
        self.teams[index_team].score = score

    def add_card(self, index_team, index_player):
        self.teams[index_team].players_at_field[index_player].cards += 1

    def replace_player(self, index_team, starter, bench):
        starter_player = self.__teams[index_team].players_at_field[starter]
        bench_player = self.__teams[index_team].players_at_bench[bench]

        # remove starter player from the match and move it to the bench
        self.__teams[index_team].players_at_field.remove(starter_player)
        self.__teams[index_team].players_at_bench.append(starter_player)

        # remove starter player from the bench and move it to the match
        self.__teams[index_team].players_at_bench.remove(bench_player)
        self.__teams[index_team].players_at_field.append(bench_player)

    def create_team(self, name, number_of_players, players_at_field, players_at_bench):
        self.__teams.append(Team(name, number_of_players, players_at_field, players_at_bench))

    # `excluded_player` é o index do radio button
    def remove_starting_player(self, min_players, titular):
        excluded_player = TeamScreen.delete_starting_player(min_players, titular)
        titular.remove(titular[excluded_player])
        return titular

    # `excluded_player` é o index do radio button
    def remove_bench_player(self, min_players, banco):
        excluded_player = TeamScreen.delete_bench_player(min_players, banco)
        print(excluded_player)
        banco.remove(banco[excluded_player])
        return banco

    def main(self, min_number_of_players):
        name, number_of_players = TeamScreen().get_data()
        #number_of_players = TeamScreen().get_number_of_players()

        while number_of_players < int(min_number_of_players):
            TeamScreen().alert_min_players(min_number_of_players)
            #number_of_players = TeamScreen().get_number_of_players()

        jogadores_linha = []
        jogadores_banco = []

        for i in range (0, min_number_of_players):
            jogadores_linha.append(PlayerController().main())

        for i in range (0, (number_of_players - min_number_of_players)):
            jogadores_banco.append(PlayerController().main())

        exit_exclude_screen = False
        while exit_exclude_screen == False:
            name, number_of_players, jogadores_linha, jogadores_banco, exit_exclude_screen = TeamScreen().confirm_team(name, number_of_players, min_number_of_players, jogadores_linha, jogadores_banco, self.remove_starting_player, self.remove_bench_player)

        self.create_team(name, number_of_players, jogadores_linha, jogadores_banco)

        return self
