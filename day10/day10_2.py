from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",")[0] for line in  f.read().splitlines()]
    return lines

def catch_spright(cycle_dic):
    display = np.zeros(240)
    for i in range(len(display)): # 0... 239
        if i == 0:
            if cycle_dic[i+1] in [i, i+1]:
                display[i] = 1
        else:
            if cycle_dic[i+1] in [i%40-1, i%40, i%40+1]:
                display[i] = 1
    return display.reshape((6, 40))


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

    res = catch_spright(cycle_dic=cycle_dic)
    plt.imshow(res)
    plt.savefig("im.png")
    



    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
