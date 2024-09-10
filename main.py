"""
PROGRAM NAME: mazes.py
PROGRAM PURPOSE: This program will generate a maze
DATE WRITTEN: 8/21/24 - 9/10/24
PROGRAMMER: Mason Kohler
"""
import prim_maze

from PIL import Image, ImageDraw


def main():
     """
     The main runtime. Is called if the program is run directly.
     returns: None
     """
     # Ask for the height and width of the maze
     height = 10
     width = 10
     pic_name = "maze.png"
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
     
     # Generate the maze
     print("Generating maze...", end=" ")
     prim_maze.generate(width, height, hori_walls, vert_walls)
     print("Maze generated!")

     # Ask user what they would like to do with the maze
     while True:
          print("What would you like to do?")
          print("1. Print maze in Terminal\n2. Save maze to image file")
          option = input(">> ")
          if option == '1':
               print_maze(hori_walls, vert_walls, width, height)
               exit()
          elif option == '2':
               print("What would you like to name the file? (ex: maze.png)")
               print("Warning! If your file already exists it will be overwritten!")
               print("Press ctrl+C if you want to cancel and exit the program")
               pic_name = input(">> ")
               print("Creating image...", end=" ")
               create_maze_image(hori_walls, vert_walls, width, height, pic_name)
               print("Image created and saved!")
               exit()
          else:
               print("Enter a valid option!")



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
     image = Image.new("RGBA", (width * 10 + 1, height * 10 + 1), (255, 255, 255, 255))
     draw = ImageDraw.Draw(image)

     # Draw the maze
     for row in range(height):
          for col in range(width):
               if hori_walls[row][col]:
                    draw.rectangle((col * 10, row * 10 - 1, (col + 1) * 10, row * 10 + 1), fill="black")
               if vert_walls[row][col]:
                    draw.rectangle((col * 10 - 1, row * 10, col * 10 + 1, (row + 1) * 10), fill="black")
               if hori_walls[row + 1][col]:
                    draw.rectangle((col * 10, (row + 1) * 10 - 1, (col + 1) * 10, (row + 1) * 10 + 1), fill="black")
               if vert_walls[row][col + 1]:
                    draw.rectangle(((col + 1) * 10 - 1, row * 10, (col + 1) * 10 + 1, (row + 1) * 10), fill="black")

     # Save the image of the maze to the named file
     # If the file name doesn't work, return an error
     try:
          image.save(f"{name}")
     except ValueError as file_ext:
          print(f"The file extension {str(file_ext)[25:]} is not supported.")
          return 1
     return 0
               

if __name__ == "__main__":
     main()