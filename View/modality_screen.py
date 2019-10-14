class ModalityScreen:
    def __init__(self):
        pass
    
    def check_valid_string_response(self, string):
        while True:
            try:
                response = input(string)
                if len(response.strip()) == 0 :
                    raise Exception()
                return response
            except Exception:
                print("\nOps, Você deve informar um nome")

    def check_valid_int_response(self, string, max_value):
        while True:
            try:
                response = int(input(string))
                if response > max_value :
                    raise Exception()
                return response
            except ValueError:
                print("\nOps, Você deve informar um número")
            except Exception:
                print("\nO número deve estar entre [0 e {max}]".format(max = max_value))

    def section_name(self):
        print('''
>>>>>>>>>> Configuração da Modalidade <<<<<<<<<<
        ''')

    def get_data(self):
        name = self.check_valid_string_response("\nQual o nome da modalidade? ")
        number_of_players = self.check_valid_int_response("\nQual o número de jogadores titulares por time? ", 10)
        gender = self.check_valid_string_response("\nQual o gênero da modalidade? ")
        return name, int(number_of_players), gender
