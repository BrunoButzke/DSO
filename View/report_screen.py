import PySimpleGUI as view


class ReportScreen:
    def __init__(self):
        pass

    def show_report(self, modality, team):

        modality_name = modality.modality.name
        gender = modality.modality.gender

        first_team = team.teams[0].name
        first_team_score = team.teams[0].score
        first_player = [[view.Text(f'Jogador número {player.number} teve {player.cards} cartões')] \
            for player in team.teams[0].players_at_field]

        second_team = team.teams[1].name
        second_team_score = team.teams[1].score
        second_player = [[view.Text(f'Jogador número {player.number} teve {player.cards} cartões')] \
            for player in team.teams[1].players_at_field]

        layout = [
                [view.Text('Equipe'), view.Text(first_team)],
                [view.Text('Pontuação:'), view.Text(first_team_score)]
            ] +\
            first_player +\
            [
                [view.Text('_' * 80)],
                [view.Text('Equipe'), view.Text(second_team)],
                [view.Text('Pontuação'), view.Text(second_team_score)]
            ] +\
            second_player +\
            [[view.Text('_' * 80)], [view.Ok()]]

        window = view.Window(f'Resultado: {modality_name} {gender}').Layout(layout)
        event, values = window.Read()
