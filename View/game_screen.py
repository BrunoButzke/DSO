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
        print('''
                    Menu de opções
            ------------------------------
            1 - Marcar pontos
            2 - Dar cartão para jogador
            3 - Substituir um jogador
            4 - Finalizar a partida
            ''')

        return self.check_valid_response("Digite o número da opção desejada: ", 4)

    def get_team(self, teams):
        string ='''
                    Times
        ------------------------------
        '''

        for team in teams:
            string += '''{index} - {number}
        '''.format(index=teams.index(team), number=team.name)

        print(string)

        return self.check_valid_response("Qual time? (informe o número): ", 1)

    def get_score(self, team_name):
        return  self.check_valid_response("\nQuantos pontos {name} deve ganhar? ".format(name = team_name), 100)

    def get_player(self, team_players):
        string = '''
                Jogadores
        -------------------------
        '''
        for player in team_players:
            string += '''{index} - {number}
        '''.format(index=team_players.index(player), number=player.number)

        print(string)

        return self.check_valid_response("\nQual jogador deve receber o cartão? ", len(team_players))

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
