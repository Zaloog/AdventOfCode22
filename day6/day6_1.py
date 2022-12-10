def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",")[0] for line in  f.read().splitlines()]
    return lines


def process_line(line, window_size):
    for win_end in range(window_size, len(line)+1):
        window = line[win_end-window_size:win_end]
        if len(set(window))==4:
            return win_end


def result(lines):
    for line in lines:
        packet_starter = process_line(line, window_size=4)
    
    res=packet_starter
    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
