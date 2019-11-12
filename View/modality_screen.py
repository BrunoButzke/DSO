import PySimpleGUI as view


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
                if response > max_value or response < 1 :
                    raise Exception()
                return response
            except ValueError:
                print("\nOps, Você deve informar um número")
            except Exception:
                print("\nO número deve estar entre [1 e {max}]".format(max = max_value))

    def section_name(self):
        print('''
>>>>>>>>>> Configuração da Modalidade <<<<<<<<<<
        ''')

    def get_data(self):

        layout = [
            [view.Text('Qual o nome da modalidade?')],
            [view.InputText()],
            [view.Text('Qual o número de jogadores titulares por time?')],
            [view.InputText()],
            [view.Text('Qual o gênero da modalidade?')],
            [view.InputText()],
            [view.Submit()]  
        ]
        window = view.Window('Modalidade').Layout(layout)
        button, values = window.Read()
        window.close()
        return values[0], int(values[1]), values[2]
        
        #name = self.check_valid_string_response("\nQual o nome da modalidade? ")
        #number_of_players = self.check_valid_int_response("\nQual o número de jogadores titulares por time? ", 10)
        #gender = self.check_valid_string_response("\nQual o gênero da modalidade? ")
        #return name, int(number_of_players), gender
        
