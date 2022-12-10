def reader(file):
    with open(file, "r") as f:
        pairs = [line.split(",") for line in  f.read().splitlines()]
    return pairs


#check if any overlap
def check_overlap(area1, area2):
    s1, e1 = [int(i) for i in area1.split("-")]
    set1 = {i for i in range(s1, e1+1)}
    s2, e2 = [int(i) for i in area2.split("-")]
    set2 = {i for i in range(s2, e2+1)}
    inters = set1.intersection(set2)
    if len(inters) > 0 :
        return 1
    else:
        return 0

def result(pairs):
    res=0
    for pair in pairs:
        res += check_overlap(pair[0], pair[1])
    return res


if __name__ == "__main__":
    pairs = reader("input.txt")
    res = result(pairs)

    print(res)



    
