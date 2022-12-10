def reader(file):
    with open(file, "r") as f:
        games = [line for line in  f.read().splitlines()]
    # A: Rock
    # B: Paper
    # C: Scissor
    p1 = [game[0] for game in games]
    # X: lose 
    # Y: draw
    # Z: win
    p2 = [game[-1] for game in games]
    # lose: 0 points
    # draw: 3 points
    # win: 6 points

    return p1, p2

# function to check points for choice
def check_choice(choice):
    point_dic = {
        "A":1,
        "B":2,
        "C":3,
        "X":1,
        "Y":2,
        "Z":3,
    }
    return point_dic[choice]

# function to check points for game result
def check_game(c1_raw, result):
    tdic = {
        "A":"Rock", # 1 point
        "B":"Paper", # 2 points
        "C":"Scissor", # 3 points
        "X":"Lose",
        "Y":"Draw",
        "Z":"Win",
        }
    c1 = tdic[c1_raw]
    result = tdic[result]
    if result == "Draw":
        return 3, check_choice(c1_raw) #score result , score_pick
    elif c1 == "Rock" and result == "Lose":
        return 0, 3
    elif c1 == "Rock" and result == "Win":
        return 6, 2
    elif c1 == "Paper" and result == "Lose":
        return 0, 1
    elif c1 == "Paper" and result == "Win":
        return 6, 3
    elif c1 == "Scissor" and result == "Lose":
        return 0, 2
    elif c1 == "Scissor" and result == "Win":
        return 6, 1
    

def result(p1, p2):
    score_result = 0
    score_choice = 0

    for c1, result in zip(p1,p2):
        score_result_turn, pick = check_game(c1, result)
        score_result += score_result_turn
        score_choice += pick

    return score_choice + score_result

if __name__ == "__main__":
    p1, p2 = reader("input.txt")
    res = result(p1, p2)
    print(res)



    
