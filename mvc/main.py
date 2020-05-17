from mvc.views.board_view import BoardView
from mvc.controllers.game_controler import GameController
from mvc.models.game_model import GameModel


def main():
    model = GameModel()
    view = BoardView('View', model)
    model.add_observer(view)
    controller = GameController(model, view)
    while controller.get_user_interaction():
        controller.model.modify()


if '__main__' == __name__:
    main()
