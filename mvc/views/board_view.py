from mvc.views.abstract_view import AbstractView
from pygame import init as game_init, display, draw

SIZE_CELL = 10
SIZE_LINE = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class BoardView(AbstractView):

    def __init__(self):
        rows = 80
        cols = 80
        x = 770
        y = 770
        game_init()
        self.screen = display.set_mode((x,y))
        display.set_caption("Gra w zycie")
        for i in range(0,cols,SIZE_CELL):
            pos = SIZE_CELL * i + SIZE_LINE/2 + SIZE_LINE * (i-1)
            draw.line(self.screen, WHITE, (pos, 0), (pos, self.screen.get_height()), SIZE_LINE)
        for i in range(0,rows,SIZE_CELL):
            pos = SIZE_CELL * i + SIZE_LINE/2 + SIZE_LINE * (i-1)
            draw.line(self.screen, WHITE, (0, pos), (self.screen.get_width(), pos), SIZE_LINE)
        display.update()

    def update(self):
        pass

    def show(self):
        pass
