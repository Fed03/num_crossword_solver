import Numberjack as NJ
from terminaltables import SingleTable


class Problem:
    def __init__(self, scheme, domain):
        self._scheme = scheme
        self._vars = NJ.Matrix(scheme.rows, scheme.cols, domain[0], domain[1])
        self._model = NJ.Model()
        self.has_solution = None

    def solve(self):
        solver = self._model.load('Mistral')
        self.has_solution = solver.solve()

        return self.has_solution

    def set_constraints(self, constraints):
        words = self._scheme.horizontal_words()
        words.update(self._scheme.vertical_words())

        for key, value in constraints.items():
            self._model.add(NJ.Sum([self._vars[row - 1][col - 1] for (row, col) in words[key]]) == value)

    def __str__(self):
        data = []
        for row_index, row in enumerate(self._vars):
            row_data = []
            for col_index, variable in enumerate(row):
                if (row_index + 1, col_index + 1) in self._scheme.blocks:
                    row_data.append('#')
                else:
                    row_data.append(variable.get_value())

            data.append(row_data)

        board = SingleTable(data)
        board.inner_row_border = True
        return board.table
