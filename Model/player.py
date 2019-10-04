class Player:
    def __init__(self, matricula, number):
        self.__matricula = matricula
        self.__number = number
        self.__cartoes = 0
    
    @property
    def matricula(self):
        return self.__matricula
        
    @property
    def number(self):
        return self.__number
    
    @property
    def cartoes(self):
        return self.__cartoes
    
    @cartoes.setter
    def cartoes(self, cartoes):
        self.cartoes = cartoes
