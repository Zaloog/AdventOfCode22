import numpy as np

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",") for line in  f.read().splitlines()]
    return lines

def to_arr(lines):
    arr = np.array([list(line[0]) for line in lines]).astype(int)
    return arr

def get_score(forrest, tree_coord):
    tree_height = forrest[tree_coord]
    # tree coord (x,y)
    y, x = tree_coord
    # calculate scenic score
    # to left
    score_left = 0
    left_trees = forrest[y, :x][::-1]
    for left_tree in left_trees: 
        if tree_height > left_tree: 
            score_left +=1
        else:
            score_left += 1
            break
    # to right
    score_right = 0
    right_trees = forrest[y, x+1:]
    for right_tree in right_trees: 
        if tree_height > right_tree: 
            score_right +=1
        else:
            score_right += 1
            break
    # up
    score_up = 0
    up_trees = forrest[:y, x][::-1]
    for up_tree in up_trees: 
        if tree_height > up_tree: 
            score_up +=1
        else:
            score_up += 1
            break

    # bottom
    score_bottom = 0
    bottom_trees = forrest[y+1:, x]
    for bottom_tree in bottom_trees: 
        if tree_height > bottom_tree: 
            score_bottom +=1
        else:
            score_bottom += 1
            break


    return score_up * score_left * score_bottom * score_right

def get_high_scores(forrest):
    # check border assume shape: n*n
    border_len = forrest.shape[0]
    visible_border = 4 * (border_len-1)

    # check inner trees
    # loop over inner trees
    score_map = np.zeros_like(forrest)
    for idy in range(1,border_len-1):
        for idx in range(1,border_len-1):
            score_map[idy, idx] = get_score(forrest=forrest, tree_coord=(idy, idx))
    highest_score = np.max(score_map)
    return highest_score




def result(lines):
    forrest = to_arr(lines)
    res=get_high_scores(forrest)
    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
