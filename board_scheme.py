class BoardScheme:
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

    def __init__(self, cols, rows, blocks):
        self.cols = cols
        self.rows = rows
        self.blocks = blocks

    def get_horizontal_words(self):
        return self.get_words(self.HORIZONTAL_DIRECTION)

    def get_vertical_words(self):
        return self.get_words(self.VERTICAL_DIRECTION)

    def get_intersections(self):
        intersections = set()
        for h_word in self.get_horizontal_words().values():
            for v_word in self.get_vertical_words().values():
                intersections.update(set(h_word).intersection(v_word))

        return intersections

    def get_words(self, direction):
        words = {}
        for first_coord in range(1, getattr(self, direction['first_pass']) + 1):
            last_block = (0, 0)

            for second_coord in range(1, getattr(self, direction['second_pass']) + 1):
                current_cell = self.get_current_cell(first_coord, second_coord, direction)

                if current_cell in self.blocks:

                    if self.block_distance(current_cell, last_block, direction) > 2:
                        key = str(len(words) + 1) + direction['key_suffix']
                        words[key] = self.generate_word(direction, first_coord, second_coord, last_block)

                    last_block = current_cell
                elif second_coord == getattr(self, direction['second_pass']) \
                        and self.block_distance(current_cell, last_block, direction) > 1:
                    key = str(len(words) + 1) + direction['key_suffix']
                    words[key] = self.generate_word(direction, first_coord, second_coord, last_block)

                    words[key].append(current_cell)

        return words

    def generate_word(self, direction, fixed_coord, variable_coord, last_block):
        last_block_index = last_block[direction['cell_index']]
        words = [(fixed_coord, index) for index in range(last_block_index + 1, variable_coord)]

        if direction != self.HORIZONTAL_DIRECTION:
            words = list(map(lambda word: word[::-1], words))

        return words

    def get_current_cell(self, first_coord, second_coord, direction):
        if direction == self.HORIZONTAL_DIRECTION:
            return first_coord, second_coord
        else:
            return second_coord, first_coord

    @staticmethod
    def block_distance(block1, block2, direction):
        return abs(block1[direction['cell_index']] - block2[direction['cell_index']])
