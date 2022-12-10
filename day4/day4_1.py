def reader(file):
    with open(file, "r") as f:
        pairs = [line.split(",") for line in  f.read().splitlines()]
    return pairs


# check for complete overlap
def check_overlap(area1, area2):
    s1, e1 = [int(i) for i in area1.split("-")]
    s2, e2 = [int(i) for i in area2.split("-")]
    # rechts in links
    if (s2 >= s1) and (e2 <= e1):
        return 1
    # links in rechts
    elif (s1 >= s2) and (e1 <= e2):
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



    
