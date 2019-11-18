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
            [view.Button(teams[0].name, key='0')],
            [view.Button(teams[1].name, key='1')]
        ]

        window = view.Window('Time').Layout(layout)
        button, values = window.Read()
        window.close()

        return int(button)

        layout = [[view.Radio(f'{team.index}' - f'{team.number}', team.index)] for team in teams]
        window = view.Window('Times').Layout(layout)
        window.close()

        return self.check_valid_response("Qual time? (informe o número): ", 1)

    def get_score(self, team_name):

        layout = [
            [view.Text('Quantos pontos f"{team_name}" deve ganhar?')],
            [view.InputText()],
            [view.Submit()]
        ]
        window = view.Window('Pontos para f"{team_name}"').Layout(layout)
        event, values = window.Read()
        window.close()
        return int(values[0])

    def get_player(self, team_players):

        headings = [
            [view.Text('Qual jogador deve receber o cartão?')]
        ] + [['Index', 'Número']]
        header =  [[view.Text(h) for h in headings]]
        radio_buttons = [
            [view.Radio(team_players.index(player), 'radio1'), view.Text(str(player.number))] for player in team_players
        ] + [[view.Submit()]]

        layout = header + radio_buttons
        window = view.Window('Jogadores').Layout(layout)
        event, values = window.Read()
        window.close()
        return int(values[0])

    def get_replacement_players(self, players_at_field, players_at_bench):
        string = '''
                Jogadores titulares
        ----------------------------------
        '''
        for player in players_at_field:
            string += '''{index} - {number}
        '''.format(index=players_at_field.index(player), number=player.number)

        string += '''

                Jogadores reservas
        ----------------------------------
        '''
        for player in players_at_bench:
            string += '''{index} - {number}
        '''.format(index=players_at_bench.index(player), number=player.number)

        print(string)

        starter_player = self.check_valid_response("\nQual jogador deve sair? ", len(players_at_field))

        bench_player = self.check_valid_response("\nQual jogador deve entrar? ", len(players_at_bench))

        return starter_player, bench_player
