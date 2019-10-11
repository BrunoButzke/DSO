class ModalityScreen:
    def __init__(self):
        pass

    def get_data(self):
        name = input("\nQual o nome da modalidade: ")
        number_players = input("\nQual o numero de jogadores titulares por time: ")
        gender = input("\nQual o genero da modalidade: ")
        return name, int(number_players), gender