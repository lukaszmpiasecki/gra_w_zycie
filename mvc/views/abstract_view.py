from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def show(self):
        pass
