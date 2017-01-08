import argparse
import json

from cw_problem.scheme import Scheme
from cw_problem.problem import Problem
from params_fetcher import *


def problem_decoder(obj):
    if 'blocks' in obj:
        obj['blocks'] = list(map(lambda x: tuple(x), obj['blocks']))
    return obj


def run(args):
    if args.cwfile:
        problem, board, problem_desc = load_problem(args.cwfile)

        print('Numeric Crosswords Solver\n')
        print('The problem consists of:')
        print('- Scheme')
        print(board)
        print('- Domains [{},{}]'.format(*problem_desc['domains']))
        print('- Definitions')
        print_definitions(problem_desc['definitions'])

        if problem.solve():
            print('\nSolved as')
            print(problem)
        else:
            print('\nThe issued problem has no solution')

    else:
        print('Numeric Crosswords Solver\n')

        rows, cols = board_size()
        blocks = board_blocks(rows, cols)

        board = Scheme(rows, cols, blocks)
        print('\nHere the board just created\n')
        print(board)

        domain = get_domain()
        problem = Problem(board, domain)

        constraints = get_constraints(board)
        problem.set_constraints(constraints)

        if problem.solve():
            print('\nSolved as')
            print(problem)
        else:
            print('\nThe issued problem has no solution')

    return


def print_definitions(definitions, indentation_lvl=2):
    for direction in ['horizontal', 'vertical']:
        print('{}{}'.format(' ' * indentation_lvl, direction))
        for key, value in definitions[direction].items():
            print('{}{}: {}'.format(' ' * (indentation_lvl + 1), key[:-1], value))


def load_problem(file):
    problem_desc = json.load(open(file), object_hook=problem_decoder)

    board = Scheme(**problem_desc['board'])
    problem = Problem(board, problem_desc['domains'])

    constraints = problem_desc['definitions']['horizontal'].copy()
    constraints.update(problem_desc['definitions']['vertical'])
    problem.set_constraints(constraints)

    return problem, board, problem_desc


parser = argparse.ArgumentParser(description='Numeric Crosswords Solver')
parser.add_argument('-cw', '--cwfile', help='A json file containing the problem definition', metavar="JSON_FILE")

run(parser.parse_args())
