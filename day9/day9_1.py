import numpy as np

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",")[0] for line in  f.read().splitlines()]
    return lines

# translate lines into movement (direction, stepsize)
def get_movement(lines):
    movement = []
    for line in lines:
        dir, step = line.split(" ")
        movement.append((dir,int(step)))
    return movement

# initiate an empty map
def initiate_empty_map(positions):
    min_idx = np.min([x for x,y in positions])
    min_idy = np.min([y for x,y in positions])

    correction = np.array((np.abs(min_idx), np.abs(min_idy)))
    corr_positions = positions + correction 

    max_idx = np.max([x for x,y in corr_positions])
    max_idy = np.max([y for x,y in corr_positions])
    size_x = max_idx + 1
    size_y = max_idy + 1

    empty_map = np.zeros((size_y, size_x))
    return empty_map, corr_positions

# check distance between tail and head
def check_distance(pos_head, pos_tail):
    dx = pos_head[0] - pos_tail[0]
    dy = pos_head[1] - pos_tail[1]
    dist = np.max([np.abs(dx), np.abs(dy)])
    return dist, dx, dy

# move heads position 
def move_head(pos_head, dir, step):
    if dir == "D":
        pos_head[1] -= step
        return pos_head
    elif dir == "U":
        pos_head[1] += step
        return pos_head
    elif dir == "R":
        pos_head[0] += step
        return pos_head
    elif dir == "L":
        pos_head[0] -= step
        return pos_head

# move tail position 
def move_tail(pos_tail, pos_head,):
    dist, dx, dy = check_distance(pos_head, pos_tail)
    # if tail is close to head no movement
    if dist <= 1:
        return pos_tail
    #if distance is greater MOOOVE!
    else:
        # non diag
        if (dx*dy) == 0 :
            pos_tail = [pos_head[0] - dx//2, pos_head[1] - dy//2]
            return pos_tail
        # diag
        else:
            if np.abs(dx) < np.abs(dy):
                pos_tail = [pos_head[0], pos_head[1] - dy//2]
                return pos_tail
            else: # np.abs(dx) > np.abs(dy)
                pos_tail = [pos_head[0] - dx//2, pos_head[1]]
                return pos_tail



# build map of places the Rope Tail visited
def build_map(moves):
    pos_head, pos_tail = [0,0], [0,0]
    # track tail positions visited
    heads_visited_pos = [[0,0]]
    tails_visited_pos = [[0,0]]
    for direction, steps in moves: 
        # 1 by 1
        for step in range(steps):
            # new pos head
            pos_head = move_head(pos_head=pos_head, dir=direction, step=1)
            heads_visited_pos.append([*pos_head])
            # new pos tail
            pos_tail = move_tail(pos_head=pos_head, pos_tail=pos_tail)
            tails_visited_pos.append([*pos_tail])
    
    # draw map of visited positions
    # init empty map
    #map, corr_positions = initiate_empty_map(heads_visited_pos)
    map, corr_positions = initiate_empty_map(tails_visited_pos)
    # update map
    for pos in corr_positions:
        map[pos[1], pos[0]] = 1

    return np.rot90(map.T)


def result(lines):
    movement = get_movement(lines)
    map = build_map(movement) 
    print(map)
    sum_visited= np.sum(map)
    res=sum_visited
    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)