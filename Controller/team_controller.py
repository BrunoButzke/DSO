from View.team_screen import TeamScreen
from Model.team import Team
from Controller.player_controller import PlayerController

class TeamController:
    def __init__(self):
        self.__teams = []
    
    @property
    def teams(self):
        return self.__teams

    def add_score(self, index_team, score):
        self.teams[index_team].score = score
    
    def add_card(self, index_team, index_player):
        self.teams[index_team].players_in_field[index_player].cards += 1
    
    def replace_player(self, index_team, titular, reserver):
        titular_player = self.__teams[index_team].players_in_field[titular]
        reserver_player = self.__teams[index_team].players_in_bank[reserver]

        self.__teams[index_team].players_in_field.remove(titular_player)
        self.__teams[index_team].players_in_bank.append(titular_player)

        self.__teams[index_team].players_in_bank.remove(reserver_player)
        self.__teams[index_team].players_in_field.append(reserver_player)

    def create_team(self, name, number_of_players, players_in_field, players_in_bank):
        self.__teams.append(Team(name, number_of_players, players_in_field, players_in_bank))

    def main(self, min_number_of_players):
        name = TeamScreen().get_name()
        number_players = TeamScreen().get_number_players()
        
        while number_players < min_number_of_players:
            TeamScreen().alert_min_players(min_number_of_players)
            number_players = TeamScreen().get_number_players()
        
        jogadores_linha = []
        jogadores_banco = []

        for i in range (0, min_number_of_players):
            jogadores_linha.append(PlayerController().main())
        
        for i in range (0, (number_players - min_number_of_players)):
            jogadores_banco.append(PlayerController().main())

        self.create_team(name, number_players, jogadores_linha, jogadores_banco)

        return self

