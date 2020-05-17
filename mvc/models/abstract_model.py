from abc import ABC, abstractmethod


class AbstractModel(ABC):

    def __init__(self):
        super().__init__()
        self._obs_list = dict()

    def add_observer(self, obs):
        if obs.name not in self._obs_list:
            self._obs_list[obs.name] = obs

    @abstractmethod
    def modify(self):
        pass

    @abstractmethod
    def notify(self):
        pass
