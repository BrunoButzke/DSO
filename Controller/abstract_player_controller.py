from abc import ABC, abstractmethod


class AbstractPlayerController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_player(self, registration, number):
        pass

    @abstractmethod
    def main(self):
        pass
