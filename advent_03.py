#Advent of code day 3
import input_module

def print_grid(grid):
    for i in range(0, len(grid)):
        print(grid[len(grid)-i-1])

def create_empty_grid(width, height):
    grid = [[0] * width for i in range(height)]
    return grid

def get_direction(direction_steps):
    return direction_steps[0:1]

def get_steps(direction_steps):
    return int(direction_steps[1:])

def walk_in_grid(start_x, start_y, direction_list, grid):
    if direction_list:
        direction_step = direction_list[0]
        direction = get_direction(direction_step)
        nr_of_steps = get_steps(direction_step)
        x = start_x
        y = start_y

        if x<0 or y<0 :
            print('x,y={0},{1}'.format(x,y)) 
            return


        for step in range(0, nr_of_steps):
            #print('{0},{1}'.format(x,y))
            grid[y][x] = grid[y][x] + 1
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
        walk_in_grid(x, y, direction_list[1:], grid)
    else:
        grid[start_y][start_x] = grid[start_y][start_x] + 1

def create_and_walk(start_x, start_y,width, height, direction_list):
    walk = create_empty_grid(width, height)
    walk_in_grid(start_x,start_y,direction_list,walk)
    return walk

def find_intersections(grid_1, grid_2):
    intersections = []
    for i in range(0,len(grid_1)):
        for j in range(0,len(grid_1[0])):
            if grid_1[i][j] > 0 and grid_2[i][j]:
                intersections.append([i,j])
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

directions = input_module.get_csv_lines_as_string_lists('input/advent_input_03.txt')
startx, starty = 7000, 10000
dim = 20000

print(startx)
print(starty)

directions_1 = directions[0]
grid_1 = create_and_walk(startx,starty,dim,dim,directions_1)

directions_2 = directions[1]
grid_2 = create_and_walk(startx,starty,dim,dim,directions_2)

intersection = find_intersections(grid_1, grid_2)
print(smallest_distance(intersection,startx, starty))