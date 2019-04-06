
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

# for debugging/visualization only
def prettyPrintGrid(grid):
    for row in grid:
        print(' '.join([str(elem) for elem in row]))


def initGrid(grid, path):
    current_x = 0
    current_y = 0
    grid[current_y][current_x] = 1 # mark starting spot
    for move in path:
        if move == 'S':
            current_y += 1
        elif move == 'E':
            current_x += 1
        grid[current_y][current_x] = 1


def find_possible_crossing(used_path):
    cross_over = 'E' if used_path[0] == 'S' else 'S'
    current_y = 0
    current_x = 0
    for idx in range(0, len(used_path)-1):
        move = used_path[idx]
        if move == 'S':
            current_y += 1
        elif move == 'E':
            current_x += 1
        
        # prevent out-of-bounds error with previousOk
        if idx == 0:
            continue

        # looking for patterns "SEE" or "ESS"
        previousOk = used_path[idx-1] != cross_over
        currentOk = used_path[idx] == cross_over
        nextOk = used_path[idx+1] == cross_over
        if previousOk and currentOk and nextOk:
            break
    return (current_y, current_x)


def doTest(test_no, grid_size, used_path):
    grid = [[0 for x in range(grid_size)] for x in range(grid_size)]
    initGrid(grid, used_path)
    # prettyPrintGrid(grid)
    used_path_first_move = used_path[0]
    used_path_last_move = used_path[len(used_path)-1]
    have_to_cross = used_path_first_move == used_path_last_move
    # print(used_path_first_move, used_path_last_move, have_to_cross)
    my_path = ""
    if have_to_cross:
        # STRATEGY : 1. find crossing opportunity
        #            2. 'walk' paralell til that point is reached (along edge)
        #            3. go straight over (edge-to-edge)
        #            4. take steps to corner (edge-to-corner)
        crossing_coords = find_possible_crossing(used_path)
        moves_before_turn = (crossing_coords[1] if used_path_first_move == 'S' else crossing_coords[0])
        # print("moves before turn", moves_before_turn, crossing_coords)
        # move til first turn
        move_dir = 'E' if used_path_first_move == 'S' else 'S'
        for idx in range(0, moves_before_turn):
            my_path += move_dir

        # flip movement direction
        move_dir = 'E' if move_dir == 'S' else 'S'

        # cross the grid (edge-to-edge)
        for idx in range(0, grid_size-1):
            my_path += move_dir

        # flip movement direction again
        move_dir = 'E' if move_dir == 'S' else 'S'

        # walk into corner (END)
        for idx in range(0, grid_size-moves_before_turn-1):
            my_path += move_dir        
    else:
        # lick the edge if we dont have to cross
        if used_path_first_move == 'S':
            for idx in range(0, grid_size-1):
                my_path += "E"
            for idx in range(0, grid_size-1):
                my_path += "S"
        elif used_path_first_move == 'E':
            for idx in range(0, grid_size-1):
                my_path += "S"
            for idx in range(0, grid_size-1):
                my_path += "E"
    print("Case #" + str(test_no) + ": " + my_path)


# ---- START OF TEST ----
# TEST: 2 , ES
# TEST: 5 , EESSSESE / ESESSESE
row_1 = input()
num_of_tests = int(row_1)
for idx in range(1, num_of_tests + 1):
    grid_size_str = input()
    used_path = input()
    doTest(idx, int(grid_size_str), used_path)
