import re
from board_scheme import BoardScheme
from crossword_problem import CrosswordsProblem


def board_size():
    question = 'Board dimension, specified as `rows, cols`\n'
    size = input('%s' % question)
    while not re.fullmatch('\d+,\s?\d+', size):
        print('Incorrect format, retry')
        size = input(question)
    return map(int, re.split(',\s?', size))


def board_blocks(row_limit, col_limit):
    question = 'List of blocks, one block at time, specified as `row_index, col_index`.'
    stop_word = 'stop'
    print(question, 'If done write `%s`' % stop_word)

    blocks = []

    block = input()
    while str(block).lower() != ('%s' % stop_word):
        if re.fullmatch('\d+,\s?\d+', block):
            block = tuple(map(int, re.split(',\s?', block)))
            if not (1 <= block[0] <= row_limit and 1 <= block[1] <= col_limit):
                print('You have exceeded the board limits')
            else:
                blocks.append(block)
        else:
            print('Incorrect format, retry')

        block = input()

    return blocks


def get_domain():
    domain = __get_domain__()
    if not 0 < domain[0] < domain[1]:
        print('Lower bound must me greater than 0')
        return get_domain()

    return domain


def __get_domain__():
    question = 'Insert the variables domain, specified as `r-s`\n'
    domain = input('%s' % question)
    while not re.fullmatch('\d+-\d+', domain):
        print('Incorrect format, retry')
        domain = input(question)

    return list(map(int, domain.split('-')))


def run():
    print('Numeric Crosswords Solver\n')

    rows, cols = board_size()
    blocks = board_blocks(rows, cols)

    board = BoardScheme(rows, cols, blocks)
    print('Here the board just created\n')
    print(board)

    domain = get_domain()
    problem = CrosswordsProblem(board, domain)

    return
