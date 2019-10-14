class GameScreen:
    def __init__(self):
        pass
    
    def check_valid_response(self, string, max_value):
        while True:
            try:
                response = int(input(string))
                if response > max_value :
                    raise Exception()
                return response
            except Exception:
                print("\nOps, Você deve informar um numero [0 á {max}]".format(max = max_value))
    
    def get_option(self):
        print('''

                    Menu de opções
            ------------------------------
            1 - Marcar pontos
            2 - Dar cartão para jogador
            3 - Substituir um jogador 
            4 - Finalizar a partida

            ''')
            
        return self.check_valid_response("\nDigite o numero da opção desejada: ", 4)

    def get_team(self, teams):
        print('''
                    Times
        ------------------------------
        0 - {name_first_team}
        1 - {name_second_team}
        '''.format(
            name_first_team = teams[0].name,
            name_second_team = teams[1].name
        ))

        return self.check_valid_response("\nQual time ? (informe o numero): ", 1) 

    def get_score(self, team_name):
        return  self.check_valid_response("\nQuantos pontos {name} deve ganhar ? ".format(name = team_name), 100) 

    def get_player(self, team_players):
        string = '''
                Jogadores
        -------------------------
        '''
        count = 0
        for player in team_players:
            string += '''{index} - {number}'''.format(index=count, number=player.number)
        
        print(string)

        return self.check_valid_response("\nQual jogador deve receber o cartão: ", len(team_players))

    def get_replacement_players(self, players_in_field, players_in_bank):
        string = '''
                Jogadores titulares
        ----------------------------------
        '''
        count = 0
        for player in players_in_field:
            string += '''{index} - {number}'''.format(index=count, number=player.number)
        
        string += '''

                Jogadores reservas
        ----------------------------------
        '''
        count = 0
        for player in players_in_bank:
            string += '''{index} - {number}'''.format(index=count, number=player.number)
        
        print(string)

        titular_player = self.check_valid_response("\nQual jogador deve sair: ", len(players_in_field))

        reserve_player = self.check_valid_response("\nQual jogador deve entrar: ", len(players_in_bank))

        return titular_player, reserve_player