import numpy as np
from collections import defaultdict

def reader(file):
    with open(file, "r") as f:
        lines = [np.array(line.split(","), dtype=int) for line in  f.read().splitlines()]
    return lines


def split_dims(lines):
    xs = np.array([line[0] for line in lines])
    print(min(xs), max(xs))
    ys = np.array([line[1] for line in lines])
    print(min(ys), max(ys))
    zs = np.array([line[2] for line in lines])
    print(min(zs), max(zs))
    return xs, ys, zs

def distance(lines):
    neighbours = defaultdict(int)
    for i,point in enumerate(lines):
        neighbours[i] = 0
        for cpoint in lines:
            dist = abs(point- cpoint)
            if sum(dist) == 1:
                neighbours[i] += 1
    return neighbours
            
def surface(neighbours):
    max_surface = 0
    for _,touch in neighbours.items():
        max_surface += (6-touch)
    return max_surface

def result(lines):
    d = distance(lines)
    split_dims(lines)
    res= surface(d)
    return res

if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
