"""
PROGRAM NAME: prim_maze.py
PROGRAM PURPOSE: This program will generate a maze using prim's algorithm
DATE WRITTEN: 8/22/24
PROGRAMMER: Mason Kohler
"""

from random import randint


def generate(width, height, hori_walls, vert_walls):
     """
     Generates a maze using the prim's algorithm
     returns: None
     """

     # 0 = cell NOT apart of maze, 1 = cell apart of maze
     global wall_list
     global cells_in_maze
     cells_in_maze = [[0 for _ in range(width)] for _ in range(height)]
     wall_list = []

     # Set the top right cell as start, and then remove create the entrance and exit
     cells_in_maze[0][0] = 1
     vert_walls[0][0] = 0
     vert_walls[height - 1][width] = 0

     # Begin the list of viable walls with the ones bordering the top left cell
     # I use a for loop in order to ensure there aren't extra embedded lists from the
     # get_cell_walls() fuction.
     for inner_list in get_cell_walls(0, 0, width, height):
          wall_list.append(inner_list)

     # This carves out the maze while there are still walls in it
     while wall_list:
          # Choose a random wall from the list of viable walls, and remove it from the
          # list. If the wall shouldn't be in the list, continue
          try:
               while True:
                    wall = wall_list.pop(randint(0, len(wall_list) - 1))
                    if wall[0] == 'hori' and cells_in_maze[wall[1]][wall[2]] == 1 and \
                    cells_in_maze[wall[1] - 1][wall[2]] == 1 or \
                    wall[0] == 'vert' and cells_in_maze[wall[1]][wall[2]] == 1 and \
                    cells_in_maze[wall[1]][wall[2] - 1] == 1:
                         continue
                    break
          # When the block of code raises a ValueError, the maze is complete
          except ValueError:
               break

          # Remove the wall from the maze
          if wall[0] == 'hori':
               hori_walls[wall[1]][wall[2]] = 0
          else:
               vert_walls[wall[1]][wall[2]] = 0

          # Mark the new room as apart of the maze
          cells_in_maze[wall[3]][wall[4]] = 1

          # Add the new walls to the list of viable walls
          for inner_list in get_cell_walls(wall[3], wall[4], width, height):
               wall_list.append(inner_list)


def get_cell_walls(row, col, width, height):
     """
     Returns a list of the walls that are around a given cell (minus outside walls) and
     have unexplored rooms beyond them.
     returns: ['hori'/'vert', wall row, wall col, cell row, cell col]
     """
     walls = []

     # Check top wall/cell
     if row > 0:
          wall = ['hori', row, col, row - 1, col]
          if cells_in_maze[row - 1][col] == 0:
               walls.append(wall)

     # Check left wall/cell
     if col > 0:
          wall = ['vert', row, col, row, col - 1]
          if cells_in_maze[row][col - 1] == 0:
               walls.append(wall)

     # Check bottom wall/cell
     if row < height - 1:
          wall = ['hori', row + 1, col, row + 1, col]
          if cells_in_maze[row + 1][col] == 0:
               walls.append(wall)

     # Check right wall/cell
     if col < width - 1:
          wall = ['vert', row, col + 1, row, col + 1]
          if cells_in_maze[row][col + 1] == 0:
               walls.append(wall)

     return walls