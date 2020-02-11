from enum import Enum


class Pieces(Enum):
    PAWN = 0
    BISHOP = 1
    KNIGHT = 2
    ROOK = 3
    QUEEN = 4


class Square(Enum):
    OBSTACLE = 0
    TARGET = 1


increments = {
    Pieces.PAWN: [(+1, -1), (+1, +1)],
    Pieces.BISHOP: [(-1, -1), (-1, +1), (+1, -1), (+1, +1)],
    Pieces.KNIGHT: [(-1, -2), (-2, -1), (-2, +1), (-1, +2), (+1, +2), (+2, +1), (+2, -1), (+1, -2)],
    Pieces.ROOK: [(+1, 0), (-1, 0), (0, -1), (0, +1)]
}
increments[Pieces.QUEEN] = increments[Pieces.BISHOP] + increments[Pieces.ROOK]


def valid_square(row, column, chessboard):
    return row in range(BOARD_SIZE) and column in range(BOARD_SIZE) and chessboard[row][column] != Square.OBSTACLE


def position_threat(piece, chessboard, increments):
    for increment in increments:
      row, column = piece[1], piece[2]
      row += increment[0]
      column += increment[1]
      if not valid_square(row, column, chessboard):
          continue
      if chessboard[row][column] == Square.TARGET:
          return True

    return False


def distance_threat(piece, chessboard, increments):
    for increment in increments:
        row, column = piece[1], piece[2]
        while True:
            row += increment[0]
            column += increment[1]

            if not valid_square(row, column, chessboard):
                break
            if chessboard[row][column] == Square.TARGET:
                return True

    return False


threat = {
    Pieces.PAWN: position_threat,
    Pieces.BISHOP: distance_threat,
    Pieces.KNIGHT: position_threat,
    Pieces.ROOK: distance_threat,
    Pieces.QUEEN: distance_threat
}


BOARD_SIZE = 8


KING = '♔'
representation = {
    '♟': Pieces.PAWN,
    '♝': Pieces.BISHOP,
    '♞': Pieces.KNIGHT,
    '♜': Pieces.ROOK,
    '♛': Pieces.QUEEN,
}


def read_chessboard(input_chessboard):
    chessboard = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    pieces = []

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            square = input_chessboard[row][column]
            # white piece
            if square in representation.keys():
                chessboard[row][column] = Square.OBSTACLE
                pieces.append((representation[square], row, column))
            # black king
            elif square == KING:
                chessboard[row][column] = Square.TARGET

    return chessboard, pieces


def check(chessboard, pieces):
    for piece in pieces:
        if threat[piece[0]](piece, chessboard, increments[piece[0]]):
            return True

    return False


def king_is_in_check(input_chessboard):
    chessboard, pieces = read_chessboard(input_chessboard)

    return check(chessboard, pieces)
