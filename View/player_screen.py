import PySimpleGUI as view

import error_boundary


class PlayerScreen:
    def __init__(self):
        pass

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

    def get_data(self):
        valid_response = False

        while not(valid_response):

            layout = [
                [view.Text('Informe a matrícula do jogador:')],
                [view.InputText()],
                [view.Text('Informe o número do jogador:')],
                [view.InputText()],
                [view.Submit()]
            ]
            window = view.Window('Jogador').Layout(layout)
            button, values = window.Read()

            registration = values[0]
            number_of_player = values[1]

            window.close()
            if(button == 'Submit'):
                valid_response = error_boundary.check_valid_string_response(registration) and error_boundary.check_valid_int_response(number_of_player, 99)
            else:
                exit(0)

        return registration, number_of_player
