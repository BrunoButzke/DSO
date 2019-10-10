class Player:
    def __init__(self, matricula, number):
        self.__matricula = matricula
        self.__number = number
        self.__cards = 0
    
    @property
    def matricula(self):
        return self.__matricula
        
    @property
    def number(self):
        return self.__number
    
    @property
    def cards(self):
        return self.__cards
    
    @cards.setter
    def cards(self, cards):
        self.__cards = cards
