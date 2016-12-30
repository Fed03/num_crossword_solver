import Numberjack as NJ


class CrosswordsProblem:
    def __init__(self, board, domain):
        self._board = board
        self._vars = NJ.Matrix(board.rows, board.cols, domain[0], domain[1])
