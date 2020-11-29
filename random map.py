def rectangle(MAT_IN, x, y, posx, posy):
    for i in range(x):
        for j in range(y):
            MAT_IN[i + posy].pop(j + posx)
            MAT_IN[i + posy].insert(j + posx, 1)
    return x / 2, y / 2


def rand_map(height, width, res, robot_size, num_obs,
             maxsize_obs):  # make sure height/res and width/res are integer or the as close as possible, all size are in meters
    import random
    import math
    map_height = round(height / res)
    map_width = round(width / res)
    obs_size_max = round(maxsize_obs / res)
    path_size = math.ceil(robot_size / res)
    print("path size:", path_size, "obs size:", obs_size_max, "*", obs_size_max)
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
                MAP[i].insert(j, 0)
    n = 0
    prev_x = 0
    prev_y = 0
    prev_posx = 0
    prev_posy = 0
    while n < num_obs:
        n = n + 1
        x = random.randint(1, obs_size_max)
        y = random.randint(1, obs_size_max)
        posx = random.randint(1, map_width - obs_size_max - 1)
        posy = random.randint(1, map_height - obs_size_max - 1)
        while prev_posx - path_size <= posx <= prev_posx + prev_x + path_size and prev_y <= posy - path_size <= prev_posy + prev_y + path_size:
            posx = random.randint(1, map_width - obs_size_max - 1)
            posy = random.randint(1, map_height - obs_size_max - 1)
        rectangle(MAP, x, y, posx, posy)
        prev_x = x
        prev_y = y
        prev_posx = posx
        prev_posy = posy

    return MAP


l = rand_map(4, 4, 0.05, 0.2, 10, 1)
for i in l:
    print(i)
