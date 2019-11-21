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

        team_name = values[0]
        total_of_players = int(values[1])

        window.close()
        return team_name, total_of_players

    def alert_min_players(self, min_players):
        print("\nAtenção: o número mínimo de jogadores deve ser igual a " + str(min_players))

    def confirm_team(self, name, number_of_players, min_players, jogadores_linha, jogadores_banco, remove_player):
        linha = [[view.Text('Jogadores titulares:')]] +\
                [[view.Text(f'- Número {jogador.number}')] for jogador in jogadores_linha]

        banco = [[view.Text('Jogadores reserva:')]] + \
                [[view.Text(f'- Número {jogador.number}')] for jogador in jogadores_banco] \
                    if len(jogadores_banco) != 0 else []

        layout = [[view.Text(f'Time: {name}')]] + \
                linha + \
                banco + \
                [[view.Submit(key='submit'), view.Button('Excluir jogador', key='delete_player')]]

        window = view.Window(f'Confirmar time {name}?').Layout(layout)
        button, values = window.Read()
        if button == 'delete_player':
            jogadores_banco = remove_player(min_players, jogadores_banco)

        window.close()
        return name, number_of_players, jogadores_linha, jogadores_banco

    def delete_player(self, jogadores_banco):
        banco = [[view.Text('Jogadores reserva:')]] + \
                [[view.Radio(f'Número {jogador.number}', f'{jogador.number}')] for jogador in jogadores_banco] \
                    if len(jogadores_banco) != 0 else []

        layout = banco + [[view.Submit()]]

        window = view.Window('Qual reserva deve ser excluído?').Layout(layout)
        button, values = window.Read()
        window.close()

        for key in values.keys():
            if values[key] == True:
                excluded_player = key
        print(excluded_player)
        return int(excluded_player)
