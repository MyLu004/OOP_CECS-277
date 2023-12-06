import random
import check_input
import rectangle

# My Lu & Andrea Vidican - CECS 277 Sec:06 & Sec:08
# 09/18/2023
# Lab 05: Moving Rectangle

'''
1.display_grid(grid)– pass in the grid and display the contents of the grid.

2. reset_grid(grid)– pass in the grid and overwrite the contents with all ‘.’s.

3. place_rect(grid, rect)– pass in the grid and the rectangle. At the location of the rectangle (x, y) on the grid, overwrite the ‘.’ characters with ‘*’s using the width and height of the rectangle.
'''

def display_grid(grid):
  for row in range(len(grid)):
    for columm in range(len(grid[row])):
      print(grid[row][columm], end=' ')
    print()

def reset_grid(grid):
  for row in range(len(grid)):
    for columm in range(len(grid[row])):
      grid[row][columm] = '.'

def place_rect(grid, rect):
  cor = myRectangle.get_coords()

  for row in range(len(grid)):
    for columm in range(len(grid[row])):
      if columm < rect[0] and row < rect[1]:
        grid[row+cor[1]][columm+cor[0]] = '*'

if __name__ == "__main__":

    '''CREATING A MAP'''
    size_map= [20,20]

    game_map = []
    for row in range(size_map[0]):
        game_map2 = []
        for columm in range(size_map[1]):
            game_map2.append(',')
        game_map.append(game_map2)


    reset_grid(game_map)

    width = check_input.get_int_range("Enter rectangle width (1-5): ",1,5) #height
    height = check_input.get_int_range('Enter rectangle height (1-5): ',1,5) #width


    myRectangle = rectangle.Rectangle(width,height)
    rect = myRectangle.get_dimensions()


    place_rect(game_map, rect) #put the rectangle in the map
    display_grid(game_map) #print out the map

    bool_cont = True #set up the bool to checking run-game

    ''' MOVING THE MAP'''
    while bool_cont:
        user_move = check_input.get_int_range("Enter Direction:\n 1. Up\n 2. Down\n 3. Left\n 4. Right\n 5. Quit \n",1,5)
        coor = myRectangle.get_coords()
        if user_move == 1: #UP [x,y-1]
            if coor[1]-1 < 0:
                pass
            else:
                myRectangle.move_up()

        elif user_move == 2: #DOWN [x,y+1]
            if coor[1]+rect[1] > size_map[0]-1:
                pass
            else:
                myRectangle.move_down()

        elif user_move == 3: #LEFT [x-1,y]
            if coor[0] - 1 < 0:
                pass
            else:
                myRectangle.move_left()

        elif user_move == 4: #RIGHT [x+1,y]
            if coor[0]+rect[0]> size_map[1]-1:
                pass
            else:
                myRectangle.move_right()

        elif user_move == 5: #QUIT THE GAME
            bool_cont = False
            break

        reset_grid(game_map)
        place_rect(game_map, rect)  # put the rectangle in the map
        display_grid(game_map)  # print out the map


print("--END OF THE GAME--")

