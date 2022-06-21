from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

# phase 1 -------------------------------------
area = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

grid = Grid(matrix=area)
start = grid.node(0, 0)
end = grid.node(9, 9)
finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)
# uses pathfinder module to find the fastest path and stores in path

print('Task 1 Solution ---')
print('Path: ' + str(path))
print('Steps: ' + str(len(path)-1))

# phase 2 -------------------------------------
from random import randint
second_area = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

i = 0
while i < 20: # changes 20 '1' elements to '0' in the second_area table, making sure to exclude the start and finish
    # nodes, adds 20 new obstacles
    random_x_coord = randint(0, 9)
    random_y_coord = randint(0, 9)
    if random_x_coord == 0 and random_y_coord == 0:
        i = i
    elif random_x_coord == 9 and random_y_coord == 9:
        i = i
    elif second_area[random_x_coord][random_y_coord] == 1:
        second_area[random_x_coord][random_y_coord] = 0
        i += 1

grid = Grid(matrix=second_area)
start = grid.node(0, 0)
end = grid.node(9, 9)
finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)
# finds the shortest path using pathfinder module and stores in path

temp_list = []
for x in range(0, 10):
    for y in range(0, 10):
        if second_area[y][x] == 0:
            temp_list.append((x, y))
# appends coordinates of the total 24 obstacles to an empty list

print('Task 2 Solution ---')
print('Obstacles: ' + str(temp_list))
if not path:
    print('Unable to reach delivery point')
else:
    print('Path: ' + str(path))