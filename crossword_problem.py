import Numberjack as NJ


class CrosswordsProblem:
    def __init__(self, board, domain):
        self._board = board
        self._vars = NJ.Matrix(board.rows, board.cols, domain[0], domain[1])
        self._model = self._build_model()

    def _build_model(self):
        return NJ.Model([self._vars[row - 1][col - 1] == 0 for (row, col) in self._board.blocks])
