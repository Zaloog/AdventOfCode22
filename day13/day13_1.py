def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",") for line in  f.read().splitlines()]
    return lines



def result(lines):
    res=0
    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
