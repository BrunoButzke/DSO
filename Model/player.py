class Player:
    def __init__(self, registration, number):
        self.__registration = registration
        self.__number = number
        self.__cards = 0

    @property
    def registration(self):
        return self.__registration

    @property
    def number(self):
        return self.__number

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = cards
