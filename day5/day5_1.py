from collections import defaultdict
import pprint

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",") for line in  f.read().splitlines()]
    return lines

def split_state_move(lines, split):
    state = lines[:split-2]
    moves = lines[split:]
    return state, moves

def parse_state(states):
    n_stacks = (len(states[0][0])+1) // 4
    stacks = defaultdict(list)
    states.reverse()
    for row in states:
        print(row)
        for stack in range(n_stacks):
            item = row[0][1 + stack*3 + stack]
            if item != " ":
                stacks[stack+1] += item

    return stacks

def parse_move(move):
    move_list = move[0].split(" ")
    # Move X
    amount = int(move_list[1])
    # From Y
    start = int(move_list[3])
    # To Z
    target = int(move_list[5])
    return  amount, start, target

def update_state(state, moves):
    new_state = state.copy()
    for move in moves:
        instruction = parse_move(move)
        amount, start, target = instruction
        print(f"move {amount} from {start} to {target}")
        print("start", new_state[start])
        print("target", new_state[target])

        # moved part
        moved = new_state[start][-amount:]
        moved.reverse()
        print("moved", moved)
        # move to new pile
        new_state[target].extend(moved)
        print("new target", new_state[target])
        # remove old pile
        print("new start", new_state[start])
        for _ in range(amount): new_state[start].pop()
        print("new start", new_state[start])

    return new_state

def get_top_items(state):

    top_list = []
    for stack in state:
        top_list.append(state[stack][-1])
    
    return "".join(top_list)


def result(lines):
    splitline = 10 
    states, moves  = split_state_move(lines, splitline)
    stacks = parse_state(states)
    final_state = update_state(stacks, moves)
    res = get_top_items(final_state)

    return res


if __name__ == "__main__":
    #lines = reader("test.txt")
    lines = reader("input.txt")

    res = result(lines)
    print(res)



    
