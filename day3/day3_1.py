def reader(file):
    with open(file, "r") as f:
        backpacks = [line for line in  f.read().splitlines()]
    return backpacks

# split backpacks in left and right part
def split(backpack):
    size = len(backpack)
    pack1 = backpack[:size//2]
    pack2 = backpack[size//2:]

    return pack1, pack2

# find common item in 2 lists
def find_double(l1, l2):
    dupl = list(set(l1).intersection(l2))
    return dupl

# get priorities of items
def get_priority(item):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    item_tmp = item.lower() 
    if item == item_tmp:
        return alpha.index(item) + 1
    else:
        return alpha.index(item_tmp) + 1 + 26

def result(backpacks):
    items = []
    for backpack in backpacks:
        p1, p2 = split(backpack)
        item = find_double(p1, p2)
        items += item
    
    prios = [get_priority(item) for item in items]
    res = sum(prios)
    return res


if __name__ == "__main__":
    backpacks = reader("input.txt")
    res = result(backpacks)

    print(res)



    
