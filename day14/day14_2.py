import numpy as np
import sys
sys.setrecursionlimit(35000)

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(" -> ") for line in  f.read().splitlines()]
        coords = [ [np.array(el.split(","), dtype=int) for el in line] for line in lines]
    return coords

class Map():

    def __init__(self, lines):
        self.lines = lines
        self.col_max = max([arr[0] for i in self.lines for arr in i]) 
        self.row_max = max([arr[1] for i in self.lines for arr in i])
        self.mapsize = (self.row_max+1 +10,self.col_max+1 + 500 ) 
        self.map = np.zeros(self.mapsize, dtype=int).astype(str)
        self.sandstart = (0, 500)
        self.n_sand = 0
    
    def build(self):
        for instr in self.lines:
            for start_line, end_line in zip(instr, instr[1:]):
                col_start, row_start  = start_line
                col_end, row_end  = end_line
                cols = sorted([col_start, col_end])
                rows = sorted([row_start, row_end])

                self.map[rows[0]:rows[1]+1, cols[0]:cols[1]+1] = "#"
        # add bottom line
        self.map[self.row_max+2, : ] = "#"

    def sand_flow(self, pos):
        row, col = pos
        while self.map[pos] != "O":
            # down
            if (self.map[row+1, col] != "#") and (self.map[row+1, col] != "O"):
                row += 1
            # diag left
            elif (self.map[row+1, col-1] != "#") and (self.map[row+1, col-1] != "O"):
                row += 1
                col -= 1
            # diag right
            elif (self.map[row+1, col+1] != "#") and (self.map[row+1, col+1] != "O"):
                row += 1
                col += 1
            # else stop
            else: 
                self.n_sand += 1
                self.map[row, col] = "O"
                # reset position
                row, col = pos



def result(lines):
    sand_start = (0, 500)
    map = Map(lines)  
    map.build()
    print(map.mapsize)
    map.sand_flow(pos=sand_start)
    res=map.n_sand

    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)