"""
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
"""

space_char = '.'
wall_char  = 'W'

def make_maze(input):
  rows = input.split("\n")
  n = len(rows)
  coords = [(x, y) for x in range(n) for y in range(n)]
  characters = "".join(rows)
  return n, dict(zip(coords, characters))

def flood_maze(maze, initial_position):
  def do_flooding(position, flooded_positions):
    if (position in maze.keys() 
        and maze[position] == space_char 
        and not position in flooded_positions
    ):
      (x,y) = position
      return do_flooding((x, y+1), 
                do_flooding((x, y-1), 
                  do_flooding((x-1, y), 
                    do_flooding((x+1, y), 
                        flooded_positions | {position}
                    )
                  )
                )
             )
    else:
      return flooded_positions
        
  return do_flooding(initial_position, set())

def path_finder(input):
  n, maze = make_maze(input)

  initial_position = (0, 0)
  flooded_positions = flood_maze(maze, initial_position)
    
  final_position = (n-1, n-1)
  return final_position in flooded_positions
