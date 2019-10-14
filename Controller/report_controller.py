class ReportController:
    def __init__(self, modality, team):
        self.__modality = modality
        self.__team = team

    def __str__(self):
        return '''
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
                modality_name=self.__modality.modality.name,
                gender=self.__modality.modality.gender,
                first_team=self.__team.teams[0].name,
                first_team_score=self.__team.teams[0].score,
                first_player_number=self.__team.teams[0].players_at_field[0].number,
                first_player_cards=self.__team.teams[0].players_at_field[0].cards,
                second_team=self.__team.teams[1].name,
                second_team_score=self.__team.teams[1].score,
                second_player_number=self.__team.teams[1].players_at_field[0].number,
                second_player_cards=self.__team.teams[1].players_at_field[0].cards
            )
