import os
import readchar
import random

pos_x = 0
pos_Y = 1
num_of_map_objects = 11

obstacle_definition = """\
##########################
                         #
###        #########     #
#####       ########     #
######
##       ##########    ###
#####      ####
#######              #####
##############
#####################
#####     ########
########
###           #########
#####     ###########    #
##########################\
"""

my_position = [1, 3]
tail_length = 0
tail = []
map_objects = []

end_game = False
died = False

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]


map_width = len(obstacle_definition[0])
map_height = len(obstacle_definition)

# Main Loop
while not end_game:
    os.system("cls")
    # Generate Random objects on the map
    while len(map_objects) < num_of_map_objects:
        new_position = [random.randint(0,map_width - 1), random.randint(0,map_height - 1)]

        if new_position not in map_objects and new_position != my_position and \
                obstacle_definition[new_position[pos_Y]][new_position[pos_x]] != "#":
             map_objects.append(new_position)



    #Draw map
    print("+" + "-" * map_width * 2 + "+")

    for coordinate_y in range(map_height):
        print("|", end="")

        for coordinate_x in range(map_width):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[pos_x] == coordinate_x and map_object[pos_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[pos_x] == coordinate_x and tail_piece[pos_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

            if my_position[pos_x] == coordinate_x and my_position[pos_Y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True
                    died = True


            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"


            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * map_width * 2 + "+")

    # Ask user where he want to move
    # Direction = WASD
    direction = readchar.readchar().decode()
    new_position = None

    if direction == "w":
        new_position = [my_position[pos_x], (my_position[pos_Y] - 1) % map_width]

    elif direction == "s":
        new_position = [my_position[pos_x], (my_position[pos_Y] + 1) % map_width]

    elif direction == "a":
        new_position = [(my_position[pos_x] - 1) % map_width, my_position[pos_Y]]

    elif direction == "d":
        new_position = [(my_position[pos_x] + 1) % map_width, my_position[pos_Y]]

    elif direction == "q":
        end_game = True


    if new_position:
        if obstacle_definition[new_position[pos_Y]][new_position[pos_x]] != "#":
            tail.insert(0, my_position.compy())
            tail = tail[:tail_length]
            my_position = new_position




if died:
    print("Has muerto! ")