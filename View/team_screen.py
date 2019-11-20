import PySimpleGUI as view


class TeamScreen:
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
                if response > max_value or response < 0 :
                    raise Exception()
                return response
            except ValueError:
                print("\nOps, Você deve informar um número")
            except Exception:
                print("\nO número deve estar entre [0 e {max}]".format(max = max_value))    

    def get_data(self):
        layout = [
            [view.Text('Qual o nome do time?')],
            [view.InputText()],
            [view.Text('Qual o número total de jogadores de sua equipe?')],
            [view.InputText()],
            [view.Submit()]  
        ]
        window = view.Window('Time').Layout(layout)
        button, values = window.Read()
        window.close()

        return values[0], int(values[1])

    def alert_min_players(self, min_players):
        print("\nAtenção: o número mínimo de jogadores deve ser igual a " + str(min_players))
