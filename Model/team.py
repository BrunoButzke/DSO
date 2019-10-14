class Team:
    def __init__(self, name, number_of_players, players_at_field, players_at_bench):
        self.__name = name
        self.__number_of_players = number_of_players
        self.__players_at_field = players_at_field
        self.__players_at_bench = players_at_bench
        self.__score = 0

    @property
    def name(self):
        return self.__name

    @property
    def number_of_players(self):
        return self.__number_of_players

    @property
    def players_at_field(self):
        return self.__players_at_field

    @property
    def players_at_bench(self):
        return self.__players_at_bench

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
