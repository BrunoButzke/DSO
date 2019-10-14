class ModalityScreen:
    def __init__(self):
        pass

    def get_data(self):
        name = input("\nQual o nome da modalidade? ")
        number_of_players = input("\nQual o número de jogadores titulares por time? ")
        gender = input("\nQual o gênero da modalidade? ")
        return name, int(number_of_players), gender
