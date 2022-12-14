import numpy as np

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
        self.mapsize = (self.row_max+1,self.col_max+1) 
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

    def sand_flow(self, pos):
        row, col = pos
        last_pos = pos
        flow = True
        while flow:
        # down
            if (self.map[row+1, col] != "#") and (self.map[row+1, col] != "O"):
                row += 1
                #self.sand_flow((row,col))
        # diag left
            elif (self.map[row+1, col-1] != "#") and (self.map[row+1, col-1] != "O"):
                row += 1
                col -= 1
                #self.sand_flow((row,col))
        # diag right
            elif (self.map[row+1, col+1] != "#") and (self.map[row+1, col+1] != "O"):
                row += 1
                col += 1
                #self.sand_flow((row,col))
        # else stop
            else: 
                self.map[row, col] = "O"
                if last_pos == (row, col):
                    flow = False
                else:
                    last_pos = (row, col)
                    self.n_sand += 1
                    try:
                        self.sand_flow(pos)
                    except IndexError:
                        break
        #self.map[pos] = "+"
        print(self.map[ 0:11, 494:504])

        pass


def result(lines):
    line_instr = lines
    sand_start = (0, 500)
    map = Map(lines)  
    map.build()
    map.sand_flow(pos=sand_start)
    res=map.n_sand

    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)