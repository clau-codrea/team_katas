from functools import reduce
from itertools import accumulate

example = [
  [' ',' ',' ',' ',' ',' ',' ','♝'],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  ['♔',' ',' ',' ',' ',' ',' ',' ']
]

"""
 Normally would import from itertools, but this version with initial
 only appears in 3.8, and codewars uses 3.6 :'(

 Uncomment if you want to run this on codewars.
"""
# def accumulate(iterable, func, *, initial=None):
#     it = iter(iterable)
#     total = initial
#     if initial is None:
#         try:
#             total = next(it)
#         except StopIteration:
#             return
#     yield total
#     for element in it:
#         total = func(total, element)
#         yield total


def makeRay(starting, nextStep, length):
    return accumulate(
        range(length),
        lambda s, _: nextStep(s),
        initial=starting
        )

def markUntilBlocked(board, ray):

    def propagateRay(state, point):
        board, blocked = state
        if (point in board.keys()
            and not blocked
            and board[point] in [' ', 'X', '♔']
        ):
          board.update([(point, 'X')])
          return (board, False)
        else:
            return (board, True)

    (newBoard, blocked) = reduce(propagateRay, ray, (board, False))
    return newBoard

def markAttackPattern(board, piece):
    (x,y), type = piece
    if type == '♟':
        board.update([((x+1,y+1), 'X'),
                      ((x-1,y+1), 'X')])
        return board
    elif type == '♜':
        hr1 = makeRay((x+1,y), lambda p: (p[0]+1, p[1]), 8)
        hr2 = makeRay((x-1,y), lambda p: (p[0]-1, p[1]), 8)
        vr1 = makeRay((x,y+1), lambda p: (p[0], p[1]+1), 8)
        vr2 = makeRay((x,y-1), lambda p: (p[0], p[1]-1), 8)
        board1 = markUntilBlocked(board, hr1)
        board2 = markUntilBlocked(board1, hr2)
        board3 = markUntilBlocked(board2, vr1)
        board4 = markUntilBlocked(board3, vr2)
        return board4
    elif type == '♞':
        points = [(x-1, y-2), (x+1, y-2), (x-1, y+2), (x+1, y+2),
                  (x-2, y-1), (x-2, y+1), (x+2, y-1), (x+2, y+1)]
        board.update([(p, 'X') for p in points])
        return board
    elif type == '♝':
        q1 = makeRay((x+1,y+1), lambda p: (p[0]+1, p[1]+1), 8)
        q2 = makeRay((x+1,y-1), lambda p: (p[0]+1, p[1]-1), 8)
        q3 = makeRay((x-1,y+1), lambda p: (p[0]-1, p[1]+1), 8)
        q4 = makeRay((x-1,y-1), lambda p: (p[0]-1, p[1]-1), 8)
        board1 = markUntilBlocked(board, q1)
        board2 = markUntilBlocked(board1, q2)
        board3 = markUntilBlocked(board2, q3)
        board4 = markUntilBlocked(board3, q4)
        return board
    elif type == '♛':
        hr1 = makeRay((x+1,y), lambda p: (p[0]+1, p[1]), 8)
        hr2 = makeRay((x-1,y), lambda p: (p[0]-1, p[1]), 8)
        vr1 = makeRay((x,y+1), lambda p: (p[0], p[1]+1), 8)
        vr2 = makeRay((x,y-1), lambda p: (p[0], p[1]-1), 8)
        q1 = makeRay((x+1,y+1), lambda p: (p[0]+1, p[1]+1), 8)
        q2 = makeRay((x+1,y-1), lambda p: (p[0]+1, p[1]-1), 8)
        q3 = makeRay((x-1,y+1), lambda p: (p[0]-1, p[1]+1), 8)
        q4 = makeRay((x-1,y-1), lambda p: (p[0]-1, p[1]-1), 8)
        board1 = markUntilBlocked(board, q1)
        board2 = markUntilBlocked(board1, q2)
        board3 = markUntilBlocked(board2, q3)
        board4 = markUntilBlocked(board3, q4)
        board5 = markUntilBlocked(board4, hr1)
        board6 = markUntilBlocked(board5, hr2)
        board7 = markUntilBlocked(board6, vr1)
        board8 = markUntilBlocked(board7, vr2)
        return board
    else:
        return board

def printBoard(board):
    for y in range(8):
        for x in range(8):
            print(board[(x,y)], end='')
        print()

def king_is_in_check(example):
    board = dict([
              ((x, y), cel)
              for (y, row) in zip(range(8), example)
              for (x, cel) in zip(range(8), row)
              ])

    pieces = [ (pos, piece)
               for (pos, piece) in board.items()
               if piece != ' ' and piece != '♔'
             ]

    result = reduce(markAttackPattern, pieces, board)
    #printBoard(result)
    return not '♔' in result.values()

print(king_is_in_check(example))
