import argparse
import json
from params_fetcher import *
from board_scheme import BoardScheme
from crossword_problem import CrosswordsProblem


def problem_decoder(obj):
    if 'blocks' in obj:
        obj['blocks'] = list(map(lambda x: tuple(x), obj['blocks']))
    return obj


def run(args):
    if args.cwfile:
        problem_desc = json.load(open(args.cwfile), object_hook=problem_decoder)

        board = BoardScheme(**problem_desc['board'])
        problem = CrosswordsProblem(board, problem_desc['domains'])

        constraints = problem_desc['definitions']['horizontal'].copy()
        constraints.update(problem_desc['definitions']['vertical'])
        problem.set_constraints(constraints)

    else:
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

run(parser.parse_args())
