HORIZONTAL_DIRECTION = {
    'key_suffix': 'h',
    'cell_index': 1,
}

VERTICAL_DIRECTION = {
    'key_suffix': 'v',
    'cell_index': 0,
}


def generate_word(direction, fixed_coord, variable_coord, last_block):
    last_block_index = last_block[direction['cell_index']]
    words = [(fixed_coord, index) for index in range(last_block_index + 1, variable_coord)]

    if direction != HORIZONTAL_DIRECTION:
        words = list(map(lambda word: word[::-1], words))

    return words


class BoardScheme:
    def __init__(self, cols, rows, blocks):
        self.cols = cols
        self.rows = rows
        self.blocks = blocks

    def get_horizontal_words(self):
        horiz_words = {}

        count = 1
        for row in range(1, self.rows + 1):
            last_block = (0, 0)
            for col in range(1, self.cols + 1):
                current_cell = (row, col)
                if current_cell in self.blocks:
                    if current_cell[1] - last_block[1] > 2:
                        key = str(count) + 'h'
                        horiz_words[key] = generate_word(HORIZONTAL_DIRECTION, row, col, last_block)
                        count += 1
                    last_block = current_cell
                elif col == self.cols and current_cell[1] - last_block[1] > 1:
                    key = str(count) + 'h'
                    horiz_words[key] = generate_word(HORIZONTAL_DIRECTION, row, col, last_block)
                    count += 1
                    horiz_words[key].append(current_cell)
        return horiz_words

    def get_vertical_words(self):
        vertical_words = {}

        count = 1
        for col in range(1, self.cols + 1):
            last_block = (0, 0)
            for row in range(1, self.rows + 1):
                current_cell = (row, col)
                if current_cell in self.blocks:
                    if current_cell[0] - last_block[0] > 2:
                        key = str(count) + 'v'
                        vertical_words[key] = generate_word(VERTICAL_DIRECTION, col, row, last_block)
                        count += 1
                    last_block = current_cell
                elif row == self.rows and current_cell[0] - last_block[0] > 1:
                    key = str(count) + 'v'
                    vertical_words[key] = [(index, col) for index in range(last_block[0] + 1, row)]
                    count += 1
                    vertical_words[key].append(current_cell)
        return vertical_words
