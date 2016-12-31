import re


def board_size():
    question = 'Board dimension, specified as `rows, cols`\n'
    size = input(question)
    while not re.fullmatch('\d+,\s?\d+', size):
        print('Incorrect format, retry')
        size = input(question)
    return map(int, re.split(',\s?', size))


def board_blocks(row_limit, col_limit):
    stop_word = 'stop'
    print('\nList of blocks, one block at time, specified as `row_index, col_index`.')
    print('If done write `{}`'.format(stop_word))

    blocks = []

    block = input()
    while str(block).lower() != stop_word:
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
    domain = _get_domain()
    if not 0 < domain[0] < domain[1]:
        print('Lower bound must me greater than 0')
        return get_domain()

    return domain


def _get_domain():
    question = '\nInsert the variables domain, specified as `r-s`\n'
    domain = input(question)
    while not re.fullmatch('\d+-\d+', domain):
        print('Incorrect format, retry')
        domain = input(question)

    return list(map(int, domain.split('-')))


def _collect_definitions(words):
    definitions = {}
    for index, word in words.items():
        definitions[index] = int(input('{} ({} cells long): '.format(index[:-1], len(word))))
    return definitions


def get_constraints(board):
    h_word = board.horizontal_words()
    v_word = board.vertical_words()

    print('Insert definitions')
    print('\nHORIZONTAL\n')
    definitions = _collect_definitions(h_word)
    print('\nVERTICAL\n')
    definitions.update(_collect_definitions(v_word))

    return definitions
