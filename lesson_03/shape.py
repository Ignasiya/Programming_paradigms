from abc import ABC, abstractmethod


class Shape(ABC):
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def __set__(self, name: str) -> None:
        self._name = name

    def __get__(self) -> str:
        return self._name

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass
