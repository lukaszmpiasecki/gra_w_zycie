from views.board_view import BoardView
from controllers.game_controler import GameController
from models.game_model import GameModel


def main():
    model = GameModel()
    view = BoardView('View', model)
    model.add_observer(view)
    controller = GameController(model, view)
    while True:
        controller.get_user_interaction()


if '__main__' == __name__:
    main()
