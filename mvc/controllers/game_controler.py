from mvc.controllers.abstract_controller import AbstractController

class GameController(AbstractController):
    def __init__(self, model:None, view:None):
        self._model = model
        self._view = view

    def get_user_interaction(self):
        user_message = input("Nacisnij n aby przejsc do nastepnej fazy lub q aby zakonczyc: \n")
        if user_message == 'n':
            self.model.modify()
        elif user_message == 'q':
            return False
        else:
            print("ERROR")
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