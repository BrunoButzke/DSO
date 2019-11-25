import PySimpleGUI as view

class GameScreen:
    def __init__(self):
        pass

    def check_valid_response(self, string, max_value):
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

    def section_name(self):
        print('''\n>>>>>>>>>> Inicializar Partida <<<<<<<<<<''')

    def get_option(self):

        layout = [
            [view.Button('Marcar Pontos', key='1')],
            [view.Button('Dar Cartão', key='2')],
            [view.Button('Substituir', key='3')],
            [view.Button('Finalizar', key='4')]
        ]
        window = view.Window('Jogo').Layout(layout)
        button, values = window.Read()
        window.close()

        return int(button)

    def get_team(self, teams):

        layout = [
            [view.Button(f'{team.name}', key=f'{teams.index(team)}')] for team in teams
        ]

        window = view.Window('Time').Layout(layout)
        button, values = window.Read()
        window.close()

        return int(button)

        if(teams[0] != None):
            first_team = [
                [view.Radio(f'{team.number}', key='0')]
            ]
        else:
            first_team = []

        if(teams[1] != None):
            second_team = [
                [view.Radio(f'{team.number}', key='1')]
            ]
        else:
            second_team = []

        layout = first_team + second_team
        window = view.Window('Time').Layout(layout)
        button, values = window.Read()
        window.close()

        return int(button)

    def get_score(self, team_name):

        layout = [
            [view.Text(f'Quantos pontos {team_name} deve ganhar?')],
            [view.InputText()],
            [view.Submit()]
        ]
        window = view.Window(f'Pontos para {team_name}').Layout(layout)
        event, values = window.Read()
        window.close()
        return int(values[0])

    def get_player(self, team_players):

        selected_field = [[view.Text("Selecione o jogador que receberá o cartão:")]] + [
            [view.Radio(f'Número {player.number}', f'{team_players.index(player)}')] for player in team_players
        ] + [[view.Submit()]]

        window = view.Window('Titulares').Layout(selected_field)
        event, values = window.Read()
        window.close()

        for key in values.keys():
            if values[key] == True:
                first_player = key

        return int(first_player)

    def get_replacement_players(self, players_at_field, players_at_bench):

        selected_field = [[view.Text("Selecione o jogador que irá sair")]] + [
            [view.Radio('Número ' + str(player.number), 'radio1')] for player in players_at_field
        ] + [[view.Submit()]]

        selected_bench = [[view.Text("Selecione o jogador que irá entrar")]] + [
            [view.Radio('Número ' + str(player.number), 'radio2')] for player in players_at_bench
        ] + [[view.Submit()]]

        window = view.Window('Titulares').Layout(selected_field)
        event, values = window.Read()
        window.close()

        for key in values.keys():
            if values[key] == True:
                first_player = key

        window = view.Window('Reservas').Layout(selected_bench)
        event, values = window.Read()
        window.close()

        for key in values.keys():
            if values[key] == True:
                second_player = key

        return first_player, second_player

        string = '''
                Jogadores titulares
        ----------------------------------
        '''
        for player in players_at_field:
            string += '''{index} - {number}
        '''.format(index=players_at_field.index(player), number=player.number)

        selected_field = [[view.Text("Selecione o jogador que ira sair")]] + [
            [view.Radio('Numero ' + str(player.number), 'radio1')] for player in players_at_field
        ] + [[view.Submit()]]

        selected_bench = [[view.Text("Selecione o jogador que ira entrar")]] + [
            [view.Radio('Numero ' + str(player.number), 'radio2')] for player in players_at_bench
        ] + [[view.Submit()]]

        window = view.Window('Titulares').Layout(selected_field)
        event, values = window.Read()
        window.close()

        for key in values.keys():
            if values[key] == True:
                first_player = key

        window = view.Window('Reservas').Layout(selected_bench)
        event, values = window.Read()
        window.close()

        for key in values.keys():
            if values[key] == True:
                second_player = key

        return int(first_player), int(second_player)
