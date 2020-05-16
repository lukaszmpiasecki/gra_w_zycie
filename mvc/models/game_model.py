from mvc.models.abstract_model import AbstractModel


class GameModel(AbstractModel):

    def __init__(self):
        super.__init__()


    def modify(self):
        pass

    def notify(self):
        for i in self.list_value():
            i.update(self)
