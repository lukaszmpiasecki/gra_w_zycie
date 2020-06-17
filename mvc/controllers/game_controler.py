from controllers.abstract_controller import AbstractController
from pygame import QUIT, quit, event

class GameController(AbstractController):
    def __init__(self, model:None, view:None):
        self._model = model
        self._view = view

    def get_user_interaction(self):
        for ev in event.get():
            if ev.type == QUIT:
                quit()
                exit()
            else:
                self.model.modify()
                return True



    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value
