from board_scheme import BoardScheme

board = BoardScheme(rows=5, cols=7, blocks=[
    (1, 3),
    (2, 5), (2, 7),
    (3, 3), (3, 4),
    (4, 2), (4, 6),
    (5, 1), (5, 7)
])

h = board.get_horizontal_words()
v = board.get_vertical_words()

print(v)