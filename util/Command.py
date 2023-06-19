from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> dict:
        pass

    @abstractmethod
    def output(self) -> dict:
        pass