from terminaltables import SingleTable

HORIZONTAL_DIRECTION = {
    'key_suffix': 'h',
    'cell_index': 1,
    'first_pass': 'rows',
    'second_pass': 'cols'
}

VERTICAL_DIRECTION = {
    'key_suffix': 'v',
    'cell_index': 0,
    'first_pass': 'cols',
    'second_pass': 'rows'
}


class Scheme:
    def __init__(self, rows, cols, blocks):
        self.cols = cols
        self.rows = rows
        self.blocks = blocks
        self._horizontal_words = self._generate_words(HORIZONTAL_DIRECTION)
        self._vertical_words = self._generate_words(VERTICAL_DIRECTION)
        self._definition_indexes = self._generate_definition_indexes()

        self.intersections = self._generate_intersections()

    def horizontal_words(self):
        definitions = {}
        for i, cell in enumerate(self._definition_indexes, 1):
            if cell in self._horizontal_words:
                definitions[str(i) + 'h'] = self._horizontal_words[cell]

        return definitions

    def vertical_words(self):
        definitions = {}
        for i, cell in enumerate(self._definition_indexes, 1):
            if cell in self._vertical_words:
                definitions[str(i) + 'v'] = self._vertical_words[cell]

        return definitions

    def _generate_definition_indexes(self):
        first_letters = list(set(self._horizontal_words.keys()).union(self._vertical_words))
        first_letters.sort(key=lambda x: x[1])  # sort on secondary key
        first_letters.sort(key=lambda x: x[0])  # then sort on primary

        return first_letters

    def _generate_intersections(self):
        intersections = set()
        for h_word in self._horizontal_words.values():
            for v_word in self._vertical_words.values():
                intersections.update(set(h_word).intersection(v_word))

        return intersections

    def _generate_words(self, direction):
        words = {}
        for x in range(1, getattr(self, direction['first_pass']) + 1):
            last_block = (0, 0)

            for y in range(1, getattr(self, direction['second_pass']) + 1):
                current_cell = _get_current_cell(x, y, direction)

                if current_cell in self.blocks:

                    if _block_distance(current_cell, last_block, direction) > 2:
                        word = _generate_word(direction, x, y, last_block)
                        words[word[0]] = word

                    last_block = current_cell
                elif y == getattr(self, direction['second_pass']) \
                        and _block_distance(current_cell, last_block, direction) > 1:
                    word = _generate_word(direction, x, y, last_block)
                    key = word[0]
                    words[key] = word

                    words[key].append(current_cell)

        return words

    def __str__(self):
        mapping = {cell: index for (index, cell) in enumerate(self._definition_indexes, start=1)}
        mapping.update({cell: '#' for cell in self.blocks})

        data = []
        for row in range(1, self.rows + 1):
            row_data = []
            for col in range(1, self.cols + 1):
                cell = (row, col)
                if cell in mapping:
                    row_data.append(mapping[cell])
                else:
                    row_data.append(' ')

            data.append(row_data)

        board = SingleTable(data)
        board.inner_row_border = True
        return board.table


def _generate_word(direction, fixed_coord, variable_coord, last_block):
    last_block_index = last_block[direction['cell_index']]
    words = [(fixed_coord, index) for index in range(last_block_index + 1, variable_coord)]

    if direction != HORIZONTAL_DIRECTION:
        words = list(map(lambda word: word[::-1], words))

    return words


def _block_distance(block1, block2, direction):
    return abs(block1[direction['cell_index']] - block2[direction['cell_index']])


def _get_current_cell(x, y, direction):
    if direction == HORIZONTAL_DIRECTION:
        return x, y
    else:
        return y, x
