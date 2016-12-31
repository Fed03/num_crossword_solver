from board_scheme import BoardScheme
from crossword_problem import CrosswordsProblem
from params_fetcher import *


def run():
    print('Numeric Crosswords Solver\n')

    rows, cols = board_size()
    blocks = board_blocks(rows, cols)

    board = BoardScheme(rows, cols, blocks)
    print('Here the board just created\n')
    print(board)

    domain = get_domain()
    problem = CrosswordsProblem(board, domain)

    constraints = get_constraints(board)
    problem.set_constraints(constraints)
    return
