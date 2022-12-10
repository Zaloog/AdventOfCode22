from pprint import pprint

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",")[0] for line in  f.read().splitlines()]
    return lines

def get_signal_strength(cycle_dic, rel_cycles):
    signal_strengths = []
    for cycle in rel_cycles:
        signal_strengths.append(cycle * cycle_dic[cycle])
    
    return sum(signal_strengths)

def result(lines):
    cycle = 1
    x = 1
    cycle_dic = {}
    for line in lines:
        if line == "noop":
            cycle_dic[cycle] = x
            cycle +=1
        elif line.startswith("add"):

            comm, amount = line.split(" ")
            amount = int(amount)
            #initiate instructions
            cycle_dic[cycle] = x
            # execute instruction
            cycle += 1
            cycle_dic[cycle] = x
            x += amount
            cycle += 1

    signal_strength_cycles = [i*40 + 20 for i in range(6)]
    res=get_signal_strength(cycle_dic, signal_strength_cycles)

    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
