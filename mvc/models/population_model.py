from mvc.models.abstract_model import AbstractModel


class PopulationModel(AbstractModel):


    def modify(self):
        pass

    def notify(self):
        for i in self.list_value():
            i.update(self)
