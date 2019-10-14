from abc import ABC, abstractmethod


class AbstractTeamController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def section_name(self):
        pass

    @abstractmethod
    def add_score(self):
        pass

    @abstractmethod
    def add_card(self):
        pass
    @abstractmethod
    def replace_player(self):
        pass

    @abstractmethod
    def create_team(self):
        pass

    @abstractmethod
    def main(self):
        pass
