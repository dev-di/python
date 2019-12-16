#Advent of code day 3
import input_module

def get_direction(direction_steps):
    return direction_steps[0:1]

def get_steps(direction_steps):
    return int(direction_steps[1:])

def add_to_coordinate(val, coordinate, coordinates):

    if not coordinate in coordinates:
        coordinates[coordinate] = 0
    else:
        print("Crossing itself at " + str(coordinate))
    coordinates[coordinate] = coordinates[coordinate] + val

def walk_in_grid(start_x, start_y, direction_list, coordinates):
    x = start_x
    y = start_y
    coordinate = (x,y)

    if direction_list:
        direction_step = direction_list[0]
        direction = get_direction(direction_step)
        nr_of_steps = get_steps(direction_step)
        
        if x<0 or y<0 :
            print('Warning: x,y={0},{1}'.format(x,y)) 
            return

        for step in range(0, nr_of_steps):
            
            coordinate = (x,y)
            add_to_coordinate(1, coordinate, coordinates)
            
            if direction == 'U':
                y = y+1
            elif direction == 'D':
                y = y-1
            elif direction == 'R':
                x = x+1
            elif direction == 'L':
                x = x-1
            else:
                print('Unknown direction!')
        walk_in_grid(x, y, direction_list[1:], coordinates)
    else:
        add_to_coordinate(1, coordinate, coordinates)

def create_and_walk(start_x, start_y,direction_list):
    coordinates = dict()
    walk_in_grid(start_x,start_y,direction_list,coordinates)
    return coordinates

def find_intersections(coordinates_1, coordinates_2):
    intersections = []
    for coordinate in coordinates_1.keys():
        if coordinate in coordinates_2:
            intersections.append(coordinate)
    return intersections

def distance(pair, start_x, start_y):
    return abs(pair[0]-start_y) + abs(pair[1]-start_x)

def distances(pair_list, start_x, start_y):
    distance_list = []
    for pair in pair_list:
        if pair[1] == start_x and pair[0] == start_y:
            print('removing starting point')
            print(pair)
        else:
            distance_list.append([pair,distance(pair, start_x, start_y)])
    return distance_list

def smallest_distance(pair_list, start_x, start_y):
    calculated_distances = distances(pair_list, start_x, start_y)
    minimum = calculated_distances[0][1]
    min_pair = calculated_distances[0][0]
    for val in calculated_distances:
        d = val[1]
        if d < minimum:
            minimum = val[1]
            min_pair = val[0]
    return [min_pair, minimum]

directions = input_module.get_csv_lines_as_string_lists('input/advent_input_03_ex_01.txt')
#directions = [["U3","R3","L1","D1","R3"],["R3","U4"]]
startx, starty = 0, 0

directions_1 = directions[0]
grid_1 = create_and_walk(startx,starty,directions_1)
print(grid_1)

directions_2 = directions[1]
grid_2 = create_and_walk(startx,starty,directions_2)
print(grid_2)

intersection = find_intersections(grid_1, grid_2)
print(intersection)
print(smallest_distance(intersection,startx, starty))