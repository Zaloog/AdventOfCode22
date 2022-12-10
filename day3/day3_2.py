def reader(file):
    with open(file, "r") as f:
        backpacks = [line for line in  f.read().splitlines()]
    return backpacks

# split backpacks into list of groups of 3
def assign_groups(backpacks):
    n_groups = len(backpacks)//3
    groups = [backpacks[i*3:i*3+3] for i in range(n_groups)  ]
    return groups

# find common item in 3 lists
def find_common(group):
    dupl = list(set(group[0]).intersection(group[1], group[2]))
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
    groups = assign_groups(backpacks)
    for group in groups:
        items += find_common(group) 
    
    prios = [get_priority(item) for item in items]
    res = sum(prios)
    return res


if __name__ == "__main__":
    backpacks = reader("input.txt")
    res = result(backpacks)
    print(res)




    
