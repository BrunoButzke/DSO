import PySimpleGUI as view


class ModalityScreen:
    def __init__(self):
        pass

    def check_valid_string_response(self, response):
        while True:
            try:
                if len(response.strip()) == 0 :
                    raise Exception()
                return response
            except Exception:
                layout = [
                    [view.Text('Ops, Você deve informar um nome')],
                    [view.Ok()]
                ]
                window = view.Window('Aviso').Layout(layout)
                button = window.Read()
                window.close()
                return False

    def check_valid_int_response(self, response, max_value):
        try:
            response = int(response)
            if response > max_value or response < 1 :
                raise Exception()
            return True
        except ValueError:
            layout = [
                [view.Text('Ops, Você deve informar um número')],
                [view.Ok()]
            ]
            window = view.Window('Aviso').Layout(layout)
            button = window.Read()
            window.close()
            return False
        except Exception:
            layout = [
                [view.Text('O número deve estar entre [1 e {max}]'.format(max = max_value))],
                [view.Ok()]
            ]
            window = view.Window('Aviso').Layout(layout)
            button = window.Read()
            window.close()
            return False

    def get_data(self):
        valid_response = False

        while not(valid_response):

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

            name = values[0]
            number_of_players = values[1]
            gender = values[2]

            window.close()
            if(button == 'Submit'):
                valid_response = self.check_valid_string_response(name) and self.check_valid_int_response(number_of_players, 7) and self.check_valid_string_response(gender) 
            else:
                exit(0)

        return name, number_of_players, gender
