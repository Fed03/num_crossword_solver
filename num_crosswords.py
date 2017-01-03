import argparse
from board_scheme import BoardScheme
from crossword_problem import CrosswordsProblem
from params_fetcher import *


def run():
    print('Numeric Crosswords Solver\n')

    rows, cols = board_size()
    blocks = board_blocks(rows, cols)

    board = BoardScheme(rows, cols, blocks)
    print('\nHere the board just created\n')
    print(board)

    domain = get_domain()
    problem = CrosswordsProblem(board, domain)

    constraints = get_constraints(board)
    problem.set_constraints(constraints)

    if problem.solve():
        pass
    else:
        print('The problem has no solution')

    return

parser = argparse.ArgumentParser(description='Numeric Crosswords Solver')
parser.add_argument('-cw', '--cwfile', help='A json file containing the problem definition', metavar="JSON_FILE")
