from abc import ABC, abstractmethod


class AbstractModel(ABC):

    @abstractmethod
    def modify(self):
        pass

    @abstractmethod
    def notify(self):
        pass
