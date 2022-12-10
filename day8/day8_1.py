import numpy as np

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",") for line in  f.read().splitlines()]
    return lines

def to_arr(lines):
    arr = np.array([list(line[0]) for line in lines]).astype(int)
    return arr

def check_visibility(forrest, tree_coord):
    tree_height = forrest[tree_coord]
    # tree coord (x,y)
    y, x = tree_coord
    # if not visible return 0, else return 1
    # check left/right
    if np.any(forrest[y, :x] >= tree_height) and np.any(forrest[y, x+1:] >= tree_height):
    # check up/down
        if np.any(forrest[:y, x] >= tree_height) and np.any(forrest[y+1:, x] >= tree_height):
            return 0
    return 1

def get_vis_sum(forrest):
    # check border assume shape: n*n
    border_len = forrest.shape[0]
    visible_border = 4 * (border_len-1)

    # check inner trees
    # loop over inner trees
    vis_map = np.zeros_like(forrest)
    for idy in range(1,border_len-1):
        for idx in range(1,border_len-1):
            vis_map[idy, idx] = check_visibility(forrest=forrest, tree_coord=(idy, idx))
    visible_inner = np.sum(vis_map)
    visible_total = visible_border + visible_inner
    return visible_total




def result(lines):
    forrest = to_arr(lines)
    res=get_vis_sum(forrest)
    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
