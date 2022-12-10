# read input file and return outputs as single lists
def reader(file):
    with open(file, "r") as f:
        games = [line for line in  f.read().splitlines()]
    # A: Rock
    # B: Paper
    # C: Scissor
    p1 = [game[0] for game in games]
    # X: Rock 1 point
    # Y: Paper 2 points
    # Z: Scissor 3 points
    p2 = [game[-1] for game in games]
    # lose: 0 points
    # draw: 3 points
    # win: 6 points
    return p1, p2

# function to check points for choice
def check_choice(choice):
    if choice == "X":
        return 1
    elif choice == "Y":
        return 2
    else:
        return 3

# function to check points for game result
def check_game(c1, c2):
    # translation dict
    tdic = {
        "A":"Rock",
        "B":"Paper",
        "C":"Scissor",
        "X":"Rock",
        "Y":"Paper",
        "Z":"Scissor",
        }
    # turn letters into Rock/Paper/Scissor
    c1 = tdic[c1]
    c2 = tdic[c2]
    if c1 == "Rock" and c2 == "Scissor":
        return 0
    elif c1 == "Rock" and c2 == "Paper":
        return 6
    elif c1 == "Paper" and c2 == "Rock":
        return 0
    elif c1 == "Paper" and c2 == "Scissor":
        return 6
    elif c1 == "Scissor" and c2 == "Paper":
        return 0
    elif c1 == "Scissor" and c2 == "Rock":
        return 6
    else:
        return 3
    

def result(p1, p2):
    score_result = 0
    score_choice = 0

    for c1, c2 in zip(p1,p2):
        score_choice += check_choice(c2)
        score_result += check_game(c1, c2)

    return score_choice + score_result

if __name__ == "__main__":
    p1, p2 = reader("input.txt")
    res = result(p1, p2)
    print(res)



    
