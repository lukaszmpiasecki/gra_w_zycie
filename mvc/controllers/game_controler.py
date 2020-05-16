from mvc.controllers.abstract_controller import AbstractController

class GameController(AbstractController):
    def __init__(self, model:None, view:None):
        super.__init__(model, view)

    def get_user_interaction(self):
        user_message = input("Nacisnij n aby przejsc do nastepnej fazy lub q aby zakonczyc: \n")
        if user_message == 'n':
            self.model.modify()
        elif user_message == 'q':
            return False
        else:
            print("ERROR")
        return True
