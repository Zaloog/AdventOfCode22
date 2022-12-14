from pprint import pprint
import ast

def reader(file):
    with open(file, "r") as f:
        lines = [line.split("\n") for line in  f.read().splitlines()]
        lines = [ast.literal_eval(line[0]) for line in lines if line != [""]]
    return lines

def get_pairs(lines):
    pairs = [(l, r) for l,r in zip(lines[::2], lines[1::2] )]
    return pairs

def compare_pairs(pl, pr):
        #print("compare", el_l, el_r)
        # both are type int
        # mixed type
        if (type(pl) == int) and (type(pr) == list):
            return compare_pairs([pl], pr)
        if (type(pl) == list) and (type(pr) == int):
            return compare_pairs(pl, [pr])
        if (type(pl) == int) and (type(pr) == int):
            if pl == pr:
                return None
            else:
                return pl < pr
        # both types are lists
        elif (type(pl) == list) and (type(pr) == list):
            for el_l, el_r in zip(pl, pr):
                x = compare_pairs(el_l, el_r)
                if x is not None:
                    return x
            return compare_pairs(len(pl), len(pr))
        

                
def result(lines):
    pairs = get_pairs(lines)
    in_order = 0
    for num, (pl,pr) in enumerate(pairs, start=1):
        print(f"pair {num}: {pl}, {pr}")
        if compare_pairs([pl], [pr]):
            in_order += num
            print("in order", num)
    res=in_order
    return res

if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)