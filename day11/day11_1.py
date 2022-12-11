import numpy as np

def reader(file):
    with open(file, "r") as f:
        lines = [[instr.strip() for instr in monkey.split("\n")] for monkey in f.read().split("\n\n")]
    return lines

def decrease_worry(worry_lv):
    return worry_lv // 3



class Monkey():

    def __init__(self, number=int ):
        self.number = number
        self.items = []
        self.ops = str
        self.test_val = int
        self.iftrue = int
        self.iffalse = int
    
    def operation(self,old):
        new = eval(self.ops)
        return new

    def test(self,old):
        if old % self.test_val == 0:
            return self.iftrue
        else:
            return self.iffalse

def init_monkeys(lines):
    monkeys = []
    for i, monkey in enumerate(lines):
        initialized_monkey = Monkey(number=i)
        for info in monkey:
            if info.startswith("Monkey"):
                number = int(info.split(" ")[1][:-1])
            elif info.startswith("Starting"):
                items = info.split(":")[1].split(",")
                items = [int(item.strip()) for item in items ]
                initialized_monkey.items = items
            elif info.startswith("Operation"):
                ops = info.split(":")[1].split("=")[1]
                initialized_monkey.ops = ops
            elif info.startswith("Test"):
                divisor = int(info.split(":")[1].split(" ")[-1])
                test = divisor
                initialized_monkey.test_val = test
            elif info.startswith("If true"):
                true_target = int(info.split(" ")[-1])
                initialized_monkey.iftrue = true_target
            elif info.startswith("If false"):
                false_target = int(info.split(" ")[-1])
                initialized_monkey.iffalse = false_target

        #initialized_monkey = Monkey(  number=number,
                                #start_items=start_items,
                                #operation=operation,
                                #test=test,
                                #iftrue=true_target,
                                #iffalse=false_target)
        monkeys.append(initialized_monkey)
    return monkeys

def let_em_play(monkeys, rounds):
    monkey_interactions = {i:0 for i,_ in enumerate(monkeys)}

    for round in range(1, rounds+1):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items[::-1]:
                # inspect
                monkey_interactions[i] += 1
                # monkey change worry
                curr_worry = monkey.operation(item)
                # decrease worry
                curr_worry = decrease_worry(curr_worry) 
                # monkey test
                throw_item_to = monkey.test(curr_worry)
                # remove item from inv
                monkey.items.pop()
                # add item to inv of target monkey
                monkeys[throw_item_to].items.append(curr_worry)

    return monkey_interactions

def calc_monkey_business(monkey_interaction):
    interactions = sorted([v for k,v in monkey_interaction.items() ])[::-1]
    return np.prod(interactions[:2])


def result(lines):
    monkeys = init_monkeys(lines)
    monkey_interaction = let_em_play(monkeys=monkeys, rounds=20)
    res = calc_monkey_business(monkey_interaction)
    return res

if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)