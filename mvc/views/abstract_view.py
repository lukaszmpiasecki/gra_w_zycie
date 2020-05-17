from abc import ABC, abstractmethod


class AbstractView(ABC):
    def __init__(self, name, model):
        super().__init__()
        self.__name = name
        self.__model = model

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def show(self):
        pass
