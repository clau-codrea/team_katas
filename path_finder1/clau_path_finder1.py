import enum


class Square(enum.Enum):
    Empty = 0
    Wall = 1
    Exit = 2


class Direction(enum.Enum):
    North = (-1, 0)
    South = (+1, 0)
    West = (0, -1)
    East = (0, +1)


def process_maze(maze_representation):
    rows = maze_representation.split()
    return {
        (row_index, col_index): type(square, (row_index, col_index), len(rows))
        for row_index, row in enumerate(rows)
        for col_index, square in enumerate(row)
    }


def type(square, position, size):
    if position == (size - 1, size - 1):
        return Square.Exit
    elif square == "W":
        return Square.Wall
    elif square == ".":
        return Square.Empty
    else:
        raise ValueError("Invalid square")


def can_reach_exit(maze):
    start_position = (0, 0)
    visited = set()

    def visit_neighbor(maze, position):
        if position in visited:
            return False
        visited.add(position)

        if maze[position] == Square.Exit:
            return True

        return any(
            visit_neighbor(maze, square)
            for square in (
                (position[0] + direction.value[0], position[1] + direction.value[1])
                for direction in Direction
            )
            if square in maze and maze[square] != Square.Wall
        )

    return visit_neighbor(maze, start_position)


def path_finder(maze_representation):
    maze = process_maze(maze_representation)

    return can_reach_exit(maze)
