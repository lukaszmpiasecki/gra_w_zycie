from models.abstract_model import AbstractModel
from random import randint


class GameModel(AbstractModel):

    def __init__(self):
        super().__init__()
        self._cell_matrix = [[0 for i in range(7)] for j in range(7)]  # macierz komorek
        self._neighbour_matrix = [[0 for i in range(7)] for j in range(7)]  # macierz ilosci sasiadow
        for i in range(7):
            for j in range(7):
                self._cell_matrix[i][j] = randint(0, 1)

    # Obliczam kto ilu ma sasiadow i wyznaczam populacje na nastepny ruch
    def modify(self):
        GameModel.count_neighbour(self)
        for i in range(7):
            for j in range(7):
                if self._neighbour_matrix[i][j] < 2 or self._neighbour_matrix[i][j] > 3:
                    self._cell_matrix[i][j] = 0
                elif self._neighbour_matrix[i][j] == 3:
                    self._cell_matrix[i][j] = 1
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self._cell_matrix)


    def count_neighbour(self):
        for i in range(7):
            for j in range(7):
                # dla komorek skrajnych przechwytuje wyjatek
                try:
                    self._neighbour_matrix[i][j] = self._cell_matrix[i - 1][j - 1] + self._cell_matrix[i - 1][j] + \
                                                   self._cell_matrix[i - 1][j + 1] + self._cell_matrix[i][j - 1] + \
                                                   self._cell_matrix[i][j + 1] + self._cell_matrix[i + 1][j - 1] + \
                                                   self._cell_matrix[i + 1][j] + self._cell_matrix[i + 1][j + 1]
                except IndexError:
                    pass
                #print(self._neighbour_matrix[i][j])

