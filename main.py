"""
PROGRAM NAME: mazes.py
PROGRAM PURPOSE: This program will generate a maze
DATE WRITTEN: 8/21/24
PROGRAMMER: Mason Kohler
"""
import prim_maze
import os

from PIL import Image, ImageDraw


def main():
     """
     The main runtime. Is called if the program is run directly.
     returns: None
     """
     # Ask for the height and width of the maze
     height = 10
     width = 10
     while True:
          try:
               print("What do you want the height of the maze to be? (2 - 100)")
               height = int(input(">> "))
               if height < 2 or height > 100:
                    raise ValueError
               break
          except ValueError:
               print("Please enter a valid number (ex: 10)")

     while True:
          try:
               print("What do you want the width of the maze to be? (2 - 100)")
               width = int(input(">> "))
               if width < 2 or width > 100:
                    raise ValueError
               break
          except ValueError:
               print("Please enter a valid number (ex: 10)")

     # Declare and define walls
     hori_walls = [[1 for _ in range(width)] for _ in range(height + 1)]
     vert_walls = [[1 for _ in range(width + 1)] for _ in range(height)]
     
     print("Generating maze...")
     prim_maze.generate(width, height, hori_walls, vert_walls)
     print("Maze generated! Would you like to do?")
     create_maze_image(hori_walls, vert_walls, width, height, "maze.png")
     # print_maze(hori_walls, vert_walls, width, height)


def print_maze(hori_walls, vert_walls, width, height):
     """
     Prints out the current maze to the screen
     returns: None
     """
     def is_wall_vert(row, col):
          """
          Checks if a verticle wall at a given location is there or not and then
          returns the correct character to print to screen
          """
          if vert_walls[row][col]:
               return "|"
          else:
               return " "

     def is_wall_hori(row, col):
          """
          Checks if a horizontal wall at a given location is there or not and then
          returns the correct character to print to screen
          """
          if hori_walls[row][col]:
               return "---"
          else:
               return "   "

     # Print the maze based on the given wall information
     for row in range(height):
          for col in range(width):
               print("+" + is_wall_hori(row, col), end="")
          print("+")

          for col in range(width):
               print(is_wall_vert(row, col) + "   ", end="")
          print(is_wall_vert(row, col + 1))
          
     for col in range(width):
          print("+" + is_wall_hori(row + 1, col), end="")
     print("+")


def create_maze_image(hori_walls, vert_walls, width, height, name):
     """
     Creates a file that is an image of the maze in a given format.
     returns: 0 for success or 1 for failure
     """
     # Create a new image with a white background and a drawing object for the image
     image = Image.new("RGB", (width * 10, height * 10), "white")
     draw = ImageDraw.Draw(image)

     # Draw the maze
     for row in range(height):
          for col in range(width):
               if hori_walls[row][col]:
                    draw.rectangle((col * 10, row * 10 - 1, (col + 1) * 10, row * 10 + 1), fill="black")
               if vert_walls[row][col]:
                    draw.rectangle((col * 10 - 1, row * 10, col * 10 + 1, (row + 1) * 10), fill="black")
     
     # Check if the file exists and ask the user if they want to replace it or change the name of the 
     # file containing the maze.
     done = False
     """
     while True:
          if os.path.exists(f"{name}"):
               while True:
                    print(f"The file {name} already exists, would you like to replace it? (y/n)")
                    check = input(">> ")
                    if check[0].lower() == 'y':
                         done = True
                         break
                    elif check[0].lower() == 'n':
                         print("What do you want to name the file?")
                         name = input(">> ")
                         break
          if done: break
     """

     try:
          image.save(f"{name}")
     except ValueError as file_ext:
          print(f"The file extension {str(file_ext)[25:]} is not supported.")
          return 1
     return 0
               



if __name__ == "__main__":
     main()