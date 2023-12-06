import random
import check_input

# My Lu & Andrea Vidican - CECS 277 Sec:06 & Sec:08
# 09/11/2023
# Lab 04: Maze Solver


def read_maze():
    """
    :param maze: Read in the contents of the file and store the content in 2D list
    :return: 2D_list [game_map] -> depend on the file

    using nested loop to go through the file and store it into the 2d list
    """
    file = open("maze.txt") #open file
    MapList2D = []
    for row in file:
        MapList = []
        for item in row:
            if item != '\n':
                MapList.append(item)
        MapList2D.append(MapList)
    file.close() #closed file

    print(MapList2D)
    return MapList2D

def find_start(maze):
    """
    :param maze: passes in the filled maze [of any size]
    :return: the location as a two item in 1D list

    Using a set of nested for loop to find an 's'
    """
    start_location = []
    for row in range(len(maze)):
        for item in range(len(maze[row])):
            if maze[row][item] == 's': #looking for 's' start pos
                start_location.append(row) #if yes, then store the idx into the start_location list. Row first
                start_location.append(item) #column [item] second
    return start_location

def display_maze(maze, loc):
    '''
    passes in the filled maze [of any size] and the user's location
    Notice: display an 'X' instead of store into the 2D_list

    maze: 2d list [game map]
    loc : 1d list [player_pos]
    '''
    for row in range(len(maze)):
        for item in range(len(maze[row])):
            if row == loc[0] and item == loc[1]: #display player location
                print('X',end='') #display X
            else:
                print(maze[row][item], end='') #print other stuff
        print()#print \n
if __name__ == "__main__":
    mapList2D = read_maze() #read file and store it into 2D list
    start_pos = find_start(mapList2D) #look for the initial pos and stored


    player_pos = [start_pos[0],start_pos[1]] #set up player_initial pos = initial pos [start location]

    print('-Maze Solver-')
    display_maze(mapList2D, player_pos) #display the map for the start

    #GAME START HERE
    while mapList2D[player_pos[0]][player_pos[1]] != 'f': #check the location with the final location
        """ QUESTION PROMPT FOR USERS"""
        print('1. Go North')
        print('2. Go South')
        print('3. Go East')
        print('4. Go West')
        player_input = check_input.get_int_range('Enter choice:',1,4) #asking player input

        if player_input == 1:
            #go to North [a-1,b] UP
            pos_check= [player_pos[0],player_pos[1]]
            print('pos checking N', (pos_check[0]) - 1, [pos_check[1]])
            print('map element', mapList2D[(pos_check[0]) - 1][pos_check[1]])

            if mapList2D[(pos_check[0])-1][pos_check[1]] == '*': #checking the wall
                print('You cannot move there') #not do anything
            else:
                player_pos = [(pos_check[0])-1,pos_check[1]] #update player_position

        elif player_input == 2:
            # go to South [a+1,b] DOWN
            pos_check = [player_pos[0],player_pos[1]]
            print('pos checking S', (pos_check[0]) + 1, [pos_check[1]])
            print('map element', mapList2D[(pos_check[0]) + 1][pos_check[1]])

            if mapList2D[(pos_check[0])+1][pos_check[1]] == '*':#checking the wall
                print('You cannot move there') #not do anything
            else:
                player_pos = [(pos_check[0])+1,pos_check[1]] #update player_position

        elif player_input == 3:
            # go to East [a,b+1] RIGHT
            pos_check = [player_pos[0],player_pos[1]]
            print('pos checking E', (pos_check[0]), (pos_check[1])+1)
            print('map element', mapList2D[(pos_check[0])][(pos_check[1]) + 1])

            if mapList2D[pos_check[0]][(pos_check[1])+1] == '*':#checking the wall
                print('You cannot move there') #not do anything
            else:
                player_pos = [(pos_check[0]), (pos_check[1])+1] #update player_position

        elif player_input == 4:
            # go to West [a,b-1] LEFT
            pos_check = [player_pos[0],player_pos[1]]
            print('pos checking W', (pos_check[0]), (pos_check[1])-1)
            print('map element', mapList2D[(pos_check[0]) + 1][(pos_check[1]) - 1])

            if mapList2D[pos_check[0]][(pos_check[1])-1] == '*':#checking the wall
                print('You cannot move there') #not do anything
            else:
                player_pos = [(pos_check[0]),(pos_check[1])-1] #update player_position


        display_maze(mapList2D, player_pos) #display the map
            #mapList2D : game map
            #player_pos: the player_pos after going through checking conditions

# OUTSIDE THE GAME
    # WINNING PRMOMPT
    print("Congratulations! You solved the maze.")
    print("---END OF THE GAME---")
