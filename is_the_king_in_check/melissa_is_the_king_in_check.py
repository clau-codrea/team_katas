def king_is_in_check(chessboard):
    pieces = ['♟', '♞', '♝', '♜', '♛']

    for row in range(len(chessboard)):
        for column in range(len(chessboard[row])):
            if chessboard[row][column] in pieces:
                char_movements, increment = choose_piece_movements(chessboard[row][column])
                if can_attack(chessboard, char_movements, row, column, increment):
                    return True

    return False

def choose_piece_movements(char):
    knight_movements = [(-1, -2), (-2, -1), (-2, +1), (-1, +2), (+1, +2), (+2, +1), (+2, -1), (+1, -2)]
    pawn_movements = [(+1, -1), (+1, +1)]
    rook_movements = [(+1, 0), (-1, 0), (0, -1), (0, +1)]
    bishop_movements = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
    queen_movements = rook_movements + bishop_movements

    if char == '♟':
        increment = False
        return pawn_movements, increment
    elif char == '♞':
        increment = False
        return knight_movements, increment
    elif char == '♝':
        increment = True
        return bishop_movements, increment
    elif char == '♜':
        increment = True
        return rook_movements, increment
    elif char == '♛':
        increment = True
        return queen_movements, increment

def can_attack(chessboard, char_movements, row, column, increment):
    is_in_check = False
    candidate_row, candidate_column = row, column
    movement_index = 0
    
    while not is_in_check and movement_index < len(char_movements):
        candidate_row, candidate_column = next_step(candidate_row, candidate_column, char_movements[movement_index])

        if is_valid(chessboard, candidate_row, candidate_column):
            is_in_check = chessboard[candidate_row][candidate_column] == '♔'
            if not increment or chessboard[candidate_row][candidate_column] != ' ' :
                movement_index += 1
                candidate_row, candidate_column = row, column
                
        else:
            movement_index += 1
            candidate_row, candidate_column = row, column

    return is_in_check

def is_valid(chessboard, row, column):
    return row in range(len(chessboard)) and column in range(len(chessboard[row]))

def next_step(row, column, movement):
    row += movement[0]
    column += movement[1]

    return row, column
    
