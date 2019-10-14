class ReportScreen:
    def __init__(self):
        pass

    def show_report(self, modality, team):
        report = '''
>>>>>>>>>> Relatório <<<<<<<<<<

                Modalidade : {modality_name} {gender}
    ----------------------------------------------
        Equipe      {first_team}
        Pontuação   {first_team_score}
        Jogador número {first_player_number} teve {first_player_cards} cartões
    ----------------------------------------------
        Equipe      {second_team}
        Pontuação   {second_team_score}
        Jogador número {second_player_number} teve {second_player_cards} cartões
        '''.format(
                modality_name=modality.modality.name,
                gender=modality.modality.gender,
                first_team=team.teams[0].name,
                first_team_score=team.teams[0].score,
                first_player_number=team.teams[0].players_at_field[0].number,
                first_player_cards=team.teams[0].players_at_field[0].cards,
                second_team=team.teams[1].name,
                second_team_score=team.teams[1].score,
                second_player_number=team.teams[1].players_at_field[0].number,
                second_player_cards=team.teams[1].players_at_field[0].cards
            )

        print(report)
