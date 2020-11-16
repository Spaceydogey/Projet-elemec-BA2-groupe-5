def rand_map(height, width, res,robot_size):  # make sure height/res and width/res are integer or the as close as possible, all size are in meters
    import random
    import math
    map_height = round(height / res)
    map_width = round(width / res)
    path_size = math.ceil(robot_size / res)
    area = map_width * map_height
    MAP = []
    '''Creation of the map'''
    for i in range(map_height):
        MAP.append([])
        for j in range(map_width):
            if i == 0 or i == map_height - 1:  # creates the top and bottom walls of the space
                MAP[i].append(1)
            elif j == 0 or j == map_width - 1:  # creates the side walls of the space
                MAP[i].append(1)
            else:  # creates random(ish) obstacle
                r = random.randint(0, 1)
                if r == 0:
                    MAP[i].insert(j, 0)
                    if j > path_size:
                        for y in range(path_size):
                            if MAP[i][j - y - 1] == 1:
                                MAP[i].pop(j - y - 1)
                                MAP[i].insert(j - y - 1, 0)
                    if i > path_size:
                        for u in range(path_size):
                            if MAP[i - u - 1][j] == 1:
                                MAP[i - u - 1].pop(j)
                                MAP[i - u - 1].insert(j, 0)
                elif r == 1:
                    if MAP[i][j - 1] == 1:
                        MAP[i].insert(j, 1)
                    else:
                        MAP[i].insert(j, random.randint(0, 1))
    for i in range(map_height):
        if 2 <= i <= map_height - 3:
            for j in range(map_width):
                if 1 <= j <= map_width - 2 and MAP[i][j] == 0 and (
                        MAP[i - 1][j] == 1 and MAP[i + 1][j] == 1 and MAP[i][j - 1] == 1 or MAP[i][j + 1] == 1 and
                        MAP[i - 1][j] == 1 and MAP[i + 1][j] == 1 or MAP[i - 1][j] == 1 and MAP[i][j - 1] == 1 and
                        MAP[i][j + 1] == 1 or MAP[i + 1][j] == 1 and MAP[i][j - 1] == 1 and MAP[i][j + 1] == 1):
                    # fill in some small holes
                    MAP[i].pop(j)
                    MAP[i].insert(j, 1)

                if 1 <= j <= map_width - 2 and MAP[i - 1][j] == 0 and MAP[i + 1][j] == 0 and MAP[i][j - 1] == 0 and \
                        MAP[i][j + 1] == 0 and MAP[i - 1][j - 1] == 0 and MAP[i + 1][j - 1] == 0 and MAP[i - 1][
                    j + 1] == 0 and MAP[i + 1][j + 1] == 0 and path_size > 1:
                    MAP[i].pop(j)
                    MAP[i].insert(j, 0)

    return MAP


l = rand_map(4, 4, 0.2, 0.2)
for i in l:
    print(i)
