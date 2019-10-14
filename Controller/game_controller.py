from View.game_screen import GameScreen

class GameController:
    def __init__(self, teams):
        self.__teams = teams
    
    def main(self):
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
                print("\n opção invalida, tente novamente")
            
    def add_score(self):
        index_team = GameScreen().get_team(self.__teams.teams)
        score = GameScreen().get_score(self.__teams.teams[index_team].name)
        self.__teams.add_score(index_team, score)
    
    def add_card(self):
        index_team = GameScreen().get_team(self.__teams.teams)
        index_player = GameScreen().get_player(self.__teams.teams[index_team].players_in_field)
        self.__teams.add_card(index_team, index_player)
    
    def replace_player(self):
        index_team = GameScreen().get_team(self.__teams.teams)
        titular, reserver = GameScreen().get_replacement_players(
            self.__teams.teams[index_team].players_in_field,
            self.__teams.teams[index_team].players_in_bank
            )
        self.__teams.replace_player(index_team, titular, reserver)
