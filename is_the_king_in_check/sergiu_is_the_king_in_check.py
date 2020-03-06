KING = u"♔"
QUEEN = u"♛"
BISHOP = u"♝"
KNIGHT = u"♞"
ROOK = u"♜"
PAWN = u"♟"
EMPTY = " "

pieces = [KING, QUEEN, BISHOP, KNIGHT, ROOK, PAWN]


def is_piece(square):
    return square != " "


def safe_get(board, i, j):
    if i < 0 or j < 0:
        return " "
    try:
        return board[i][j]
    except:
        return " "


def to_the_right(board, line, column):
    for square in board[line][column + 1 : 8]:
        if is_piece(square):
            return square


def to_the_left(board, line, column):
    for square in board[line][column - 1 :: -1]:
        if is_piece(square):
            return square


def horizontal(board, line, column):
    line_of_sight = []
    if column > 0:
        piece = to_the_left(board, line, column)
        if piece is not None:
            line_of_sight.append(piece)
    if column < 7:
        piece = to_the_right(board, line, column)
        if piece is not None:
            line_of_sight.append(piece)
    return line_of_sight


def upwards(board, line, column):
    for row in board[line - 1 :: -1]:
        if is_piece(row[column]):
            return row[column]


def downwards(board, line, column):
    for row in board[line + 1 : 8]:
        if is_piece(row[column]):
            return row[column]


def vertical(board, line, column):
    line_of_sight = []
    if line > 0:
        piece = upwards(board, line, column)
        if piece is not None:
            line_of_sight.append(piece)
    if line < 7:
        piece = downwards(board, line, column)
        if piece is not None:
            line_of_sight.append(piece)
    return line_of_sight


def main_diagonal(board, line, column):
    line_of_sight = []
    for i in range(1, 8):
        square = safe_get(board, line - i, column - i)
        if square != " ":
            line_of_sight.append(square)
            break
    for i in range(1, 8):
        square = safe_get(board, line + i, column + i)
        if square != " ":
            line_of_sight.append(square)
            break
    return line_of_sight


def second_diagonal(board, line, column):
    line_of_sight = []
    for i in range(1, 8):
        square = safe_get(board, line - i, column + i)
        if square != " ":
            line_of_sight.append(square)
            break
    for i in range(1, 8):
        square = safe_get(board, line + i, column - i)
        if square != " ":
            line_of_sight.append(square)
            break
    return line_of_sight


def line_of_sight(piece, board, position):
    line, column = position
    if piece == QUEEN:
        return (
            horizontal(board, line, column)
            + vertical(board, line, column)
            + main_diagonal(board, line, column)
            + second_diagonal(board, line, column)
        )
    if piece == ROOK:
        return horizontal(board, line, column) + vertical(board, line, column)
    if piece == PAWN:
        return [
            safe_get(board, line + 1, column - 1),
            safe_get(board, line + 1, column + 1),
        ]
    if piece == KNIGHT:
        positions = [
            (line + 1, column + 2),
            (line + 1, column - 2),
            (line - 1, column + 2),
            (line - 1, column - 2),
            (line + 2, column + 1),
            (line + 2, column - 1),
            (line - 2, column + 1),
            (line - 2, column - 1),
        ]
        return [safe_get(board, i, j) for (i, j) in positions]
    if piece == BISHOP:
        return main_diagonal(board, line, column) + second_diagonal(board, line, column)


def is_king_in_line_of_sight(piece, board, position):
    return KING in line_of_sight(piece, board, position)


def king_is_in_check(chessboard):
    for i, line in enumerate(chessboard):
        for j, square in enumerate(line):
            if square != " " and square != KING:
                if is_king_in_line_of_sight(square, chessboard, (i, j)):
                    return True
    return False
