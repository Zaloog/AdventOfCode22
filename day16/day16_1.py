from pprint import pprint
import numpy as np
from collections import defaultdict

def reader(file):
    with open(file, "r") as f:
        #lines = [line for line in  f.read().splitlines()]
        lines = f.read().splitlines()
    return lines

def extract_infos(lines):
    valves = {}
    for line in lines:
        valve_name = line.split(" ")[1]
        flowrate = int(line.split("flow rate=")[1].split(";")[0])
        lead2 = line.split("to valv")[1].replace(",", "").split(" ")[1:]

        valves[valve_name] = Valve(name=valve_name, flowrate=flowrate, connected=lead2)
    return valves

class Valve():

    def __init__(self, name, connected, flowrate):
        self.name = name
        self.connected = connected
        self.flowrate = flowrate
        self.open = False
        self.pressure_released = 0
    
    def open_valve(self, t):
        self.open = True
        self.pressure_released = self.flowrate * t

class Piping_System():

    def __init__(self, valves):
        self.valves = valves
        self.time = 30
        self.dist_matrix = defaultdict(dict)

    def total_pressure(self):
        return sum([valve.pressure_released for _, valve in self.valves.items()])

    def get_distances(self):
        # initial dist matrix
        for valve_name, valve in self.valves.items():
            self.dist_matrix[valve_name][valve_name] = 0
            for neigh_valve in valve.connected:
                self.dist_matrix[valve_name][neigh_valve] = 1
                self.dist_matrix[neigh_valve][valve_name] = 1
                for rooms in self.valves:
                    if (valve_name in self.dist_matrix[rooms]) and (neigh_valve not in self.dist_matrix[rooms]):
                        self.dist_matrix[rooms][neigh_valve] = self.dist_matrix[rooms][valve_name] + 1
                        self.dist_matrix[neigh_valve][rooms] = self.dist_matrix[rooms][neigh_valve]

    def distance_between(self, current_pos, target_position):
        return self.dist_matrix[current_pos][target_position]

    def move_to_best_expected_score(self, pos):
        score = {}
        totalscore1 = {}
        totalscore2 = {}
        for valve_name, valve in self.valves.items():
            if (valve_name == pos) or (valve.flowrate == 0):
                continue
            if valve.open:
                score[valve_name] = 0
                totalscore1[valve_name] = 0
                totalscore2[valve_name] = 0
            else:
                score[valve_name] = (self.time-self.distance_between(pos,valve_name)-1) * valve.flowrate
                totalscore1[valve_name] = 0
                totalscore2[valve_name] = 0
                # next level 1
                next_lv_score1 = []
                for  next_valve, nvalve in self.valves.items():
                    if next_valve in [valve_name, pos]:
                        continue
                    next_lv_score1.append(  (self.time-self.distance_between(pos,valve_name) 
                                    - self.distance_between(valve_name,next_valve) -1) * nvalve.flowrate)

                    # next level 2
                    next_lv_score2 = []
                    for  next_valve2, nvalve2 in self.valves.items():
                        if next_valve2 in [valve_name, pos, next_valve]:
                            continue
                        next_lv_score2.append(  (self.time-self.distance_between(pos,valve_name) 
                                        - self.distance_between(valve_name,next_valve) -1
                                        - self.distance_between(next_valve, next_valve2)) * nvalve2.flowrate)
                    if totalscore2[valve_name] < max(next_lv_score2):
                        totalscore2[valve_name] = max(next_lv_score2)
                totalscore1[valve_name] = max(next_lv_score1) + score[valve_name]
            totalscore2[valve_name] += totalscore1[valve_name] 
                    
            #print(f"score {valve_name}", score[valve_name])
            #print(f"score1 {valve_name}", totalscore1[valve_name])
            #print(f"score2 {valve_name}", totalscore2[valve_name])

        #score  = {k:v for k,v in sorted(score.items(), key=lambda kv: kv[1], reverse=True)}
        score  = {k:v for k,v in sorted(totalscore2.items(), key=lambda kv: kv[1], reverse=True)}
        new_pos = list(score.keys())[0]

        self.time -= self.distance_between(pos, new_pos)
        sum_score = sum([val for _, val in score.items()])
        return new_pos, sum_score

    def play_with_pipes(self, start="AA"):
        rel_rooms = [name for name, valve_0 in self.valves.items() if valve_0.flowrate != 0] + [start]
        pos = start
        # build dist matrix
        self.get_distances()

        print(f"Start at valve {start}")
        while self.time > 0:
            #print(f"At time {self.time} At pos {pos}")
            #print(f"----------- Minute{self.time} ----------")
            # Moving
            if self.valves[pos].open or self.valves[pos].flowrate == 0:
                new_pos, sum_score = self.move_to_best_expected_score(pos=pos)
                print(f"Move from {pos} to {new_pos}")
                pos = new_pos
                if sum_score == 0:
                    break
            # opening
            elif self.valves[pos].open == False:
                self.valves[pos].open_valve(t=self.time - 1)
                self.time -= 1
                #print(f"Open valve {pos} with FR {self.valves[pos].flowrate}")
                #print(f"Pressure released {self.valves[pos].pressure_released}")
            else:
                self.time -= 1


def result(lines):
    valves = extract_infos(lines)
    system = Piping_System(valves=valves)
    system.play_with_pipes(start="AA")
    system.get_distances()

    res=system.total_pressure()
    print("blub", )
    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(f"Total Pressure relased {res}/1651 --- {res/1651*100:.2f}%" )
