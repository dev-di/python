#Advent of code day 3
import input_module
from functools import reduce

def get_direction(direction_steps):
    return direction_steps[0:1]

def get_steps(direction_steps):
    return int(direction_steps[1:])

def add_to_coordinate(val, coordinate, coordinates):
    if not coordinate in coordinates:
        coordinates[coordinate] = val

def walk_in_grid(start_x, start_y, direction_list, coordinates, order):
    x = start_x
    y = start_y
    coordinate = (x,y)
    current_order = order

    if direction_list:
        direction_step = direction_list[0]
        direction = get_direction(direction_step)
        nr_of_steps = get_steps(direction_step)
        
        for step in range(0, nr_of_steps):
            
            coordinate = (x,y)
            add_to_coordinate(current_order, coordinate, coordinates)
            current_order = current_order+1

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
        walk_in_grid(x, y, direction_list[1:], coordinates, current_order)
    else: #Adding the last step
        add_to_coordinate(current_order, coordinate, coordinates)

def create_and_walk(start_x, start_y, direction_list):
    coordinates = dict()
    walk_in_grid(start_x, start_y, direction_list, coordinates, 0)
    return coordinates

def find_intersections(coordinates_1, coordinates_2):
    intersections = []
    for coordinate in coordinates_1.keys():
        if coordinate in coordinates_2:
            intersections.append(coordinate)
    return intersections

def find_intersections_distances(coordinates_1, coordinates_2):
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

def distance_sums(distances, coordinates_1, coordinates_2):
    lista = []
    for coordinate in distances:
        ds = coordinates_1[coordinate] + coordinates_2[coordinate]
        lista.append((coordinate, ds))
    return lista

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

def smallest_distance_sum(coordinate_dist_list):
    minimum = coordinate_dist_list[0][1]
    min_pair = coordinate_dist_list[0][0]
    #print(minimum)
    #print(min_pair)
    for val in coordinate_dist_list:
        dist = val[1]
        if dist < minimum:
            dist = val[1]
            min_pair = val[0]
    return [min_pair, minimum]

directions = input_module.get_csv_lines_as_string_lists('input/advent_input_03.txt')
#directions = [["U3","R3","L1","D1","R3"],["R3","U4"]]
startx, starty = 0, 0

directions_1 = directions[0]
grid_1 = create_and_walk(startx,starty,directions_1)
#print(grid_1)

directions_2 = directions[1]
grid_2 = create_and_walk(startx,starty,directions_2)
#print(grid_2)

intersections = find_intersections(grid_1, grid_2)
print("Intersections")
#print(intersections)

#print(smallest_distance(intersections,startx, starty))

distancesums = distance_sums(intersections, grid_1, grid_2)

print(smallest_distance_sum(distancesums[1:]))
