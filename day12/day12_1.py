import numpy as np
from string import ascii_lowercase

def reader(file):
    with open(file, "r") as f:
        lines = [list(line.split(",")[0]) for line in  f.read().splitlines()]
    return lines

def to_arr(lines):
    arr = np.array(lines)
    return arr

class Elevation_Map():

    def __init__(self, arr):
        self.map = arr
        self.x_max = self.map.shape[1]
        self.y_max = self.map.shape[0]
        self.start = tuple(i[0] for i in np.where(self.map == "S"))
        self.end = tuple(i[0] for i in np.where(self.map == "E"))
        self.reward_map = np.zeros_like(self.map, dtype=int).astype(str)
        self.steps = 0
    
    def __repr__(self) -> str:
        return f"{self.map}"
    
    def lv(self, coords):
        return self.map[coords]

    def get_steps(self, coords):
        return self.reward_map[coords]

    def in_distance(self, lv, neigh_lv):
        if lv == neigh_lv:
            return True
        letters = ["S"] + [l for l in ascii_lowercase] + ["E"]
        #letters.reverse()
        #letter_checks = [(act,hi) for act, hi in zip(letters, letters[1:])]
        letter_checks = {letter:num for num, letter in enumerate(letters)}
        if letter_checks[neigh_lv] <= (letter_checks[lv]+1): 
            return True
        else: 
            return False
    
    def neighbours(self, coords):
        x, y = coords
        lv = self.lv(coords)
        # check right
        pos_r = (x + 1, y)
        # check left
        pos_l = (x - 1, y)
        # check down
        pos_d = (x, y + 1)
        # check up
        pos_u = (x, y - 1)

        pot_neighbours = [pos_r, pos_l, pos_u, pos_d]
        real_neighbours = []
        for pos in pot_neighbours:
            # nicht im randbereich
            if (pos[0] in range(self.y_max)) and (pos[1] in range(self.x_max)):
                neigh_lv = self.lv(pos)
                #restr1 step schon vorhanden
                #restr2 alphabet order
                if (self.get_steps(pos) == "0") and self.in_distance(lv, neigh_lv):
                    real_neighbours.append(pos)
        return real_neighbours

    
    def build_reward_map(self):
        def calc_steps(fields, steps):
            valid_neighbours = []
            for field in fields:
                self.reward_map[field] = str(steps)
                valid_neighbours.extend(self.neighbours(field))
                if self.lv(field) == "E":
                    print(steps)
                    return self.steps
            self.steps += 1
            valid_neighbours = list(set([i for i in valid_neighbours]))
            try:
                calc_steps(valid_neighbours, steps=self.steps)
            except RecursionError:
                pass

        calc_steps(fields=[self.start], steps=self.steps)



def result(arr):
    # build rew map 
    elev_map = Elevation_Map(arr=arr)
    elev_map.build_reward_map()
    E = elev_map.end
    print(elev_map.map)
    print("#"*50)
    print(elev_map.reward_map)
    res=elev_map.reward_map[E]
    return res

if __name__ == "__main__":
    lines = reader("test.txt")
    arr = to_arr(lines=lines)
    res = result(arr)

    print(res)