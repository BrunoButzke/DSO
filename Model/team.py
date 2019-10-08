class Team:
    def __init__(self, name, number_of_players, players_in_field, players_in_bank):
        self.__name = name
        self.__number_of_players = number_of_players
        self.__players_in_field = players_in_field
        self.__players_in_bank = players_in_bank
        self.__score = 0

    @property
    def name(self):
        return self.__name
    
    @property
    def number_of_players(self):
        return self.__number_of_players
    
    @property
    def players_in_field(self):
        return self.__players_in_field
    
    @property
    def players_in_bank(self):
        return self.__players_in_bank
    
    @property
    def score(self):
        return self.__score 
    
    @score.setter
    def score(self, score):
        self.__score = score