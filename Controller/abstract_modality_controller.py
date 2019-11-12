from abc import ABC, abstractmethod


class AbstractModalityController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_modality(self):
        pass

    @abstractmethod
    def main(self):
        pass
