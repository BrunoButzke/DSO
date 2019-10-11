class TeamScreen:
    def __init__(self):
        pass

    def get_name(self):
        name = input('qual o nome do time ?')
        return name
        
    def get_number_players(self):
        number_players = input("\nQual o numero total de jogadores de sua equipe: ")
        return int(number_players)

    def alert_min_players(self, min_players):
        print("\nAtenção, o numero minimo de jogadores deve ser igual a " + str(min_players))