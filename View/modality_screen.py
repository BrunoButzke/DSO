class ModalityScreen:
    def __init__(self):
        pass

    def get_data(self):
        name = input("qual o nome da modalidade ?")
        number_players = input("qual o numero maximo de jogadores por time ?")
        gender = input("qual o genero da modalidade")
        return name, int(number_players), gender