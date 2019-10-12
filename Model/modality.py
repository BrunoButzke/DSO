class Modality:
    def __init__(self, name, number_of_players_per_team, gender):
        self.__name = name
        self.__number_of_players = number_of_players_per_team
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def number_of_players(self):
        return self.__number_of_players

    @property
    def gender(self):
        return self.__gender
