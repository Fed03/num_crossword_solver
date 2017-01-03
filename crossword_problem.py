import Numberjack as NJ


class CrosswordsProblem:
    def __init__(self, board, domain):
        self._board = board
        self._vars = NJ.Matrix(board.rows, board.cols, domain[0], domain[1])
        self._model = NJ.Model()
        self.has_solution = None

    def solve(self):
        solver = self._model.load('Mistral')
        self.has_solution = solver.solve()

        return self.has_solution

    def set_constraints(self, constraints):
        words = self._board.horizontal_words()
        words.update(self._board.vertical_words())

        for key, value in constraints.items():
            self._model.add(NJ.Sum([self._vars[row - 1][col - 1] for (row, col) in words[key]]) == value)

    # def _build_model(self):
    #     return NJ.Model()
