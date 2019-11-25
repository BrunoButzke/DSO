import PySimpleGUI as view

import error_boundary


class ModalityScreen:
    def __init__(self):
        pass

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
                valid_response = error_boundary.check_valid_string_response(name) and error_boundary.check_valid_int_response(number_of_players, 7) and error_boundary.check_valid_string_response(gender)
            else:
                exit(0)

        return name, number_of_players, gender
