class TeamScreen:
    def __init__(self):
        pass

    def get_name(self):
        name = input('Qual o nome do time?')
        return name

    def get_number_of_players(self):
        number_of_players = input("\nQual o número total de jogadores de sua equipe? ")
        return int(number_of_players)

    def alert_min_players(self, min_players):
        print("\nAtenção: o número mínimo de jogadores deve ser igual a " + str(min_players))
