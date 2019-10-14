from View.report_screen import ReportScreen


class ReportController:
    def __init__(self, modality, team):
        self.__modality = modality
        self.__team = team

    def show_report(self):
        ReportScreen().show_report(self.__modality, self.__team)
