from abc import ABC, abstractmethod


class AbstractModel(ABC):

    def __init__(self):
        super.__init__()

    @abstractmethod
    def modify(self):
        pass

    @abstractmethod
    def notify(self):
        pass
