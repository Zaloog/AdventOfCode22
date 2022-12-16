import numpy as np
from scipy.spatial.distance import cdist
from tqdm import trange


def reader(file):
    with open(file, "r") as f:
        lines = [line for line in  f.read().splitlines()]
    return lines

def l2coords(lines, target_line):
    sb_on_line = set()
    sensors = []
    beacons = []
    for line in lines:
        sensor_x = line.split("x=")[1].split(",")[0]
        sensor_y = line.split("y=")[1].split(":")[0]
        beacon_x = line.split("x=")[2].split(",")[0]
        beacon_y = line.split("y=")[2]
        sensors.append((int(sensor_x),int(sensor_y)))
        beacons.append((int(beacon_x),int(beacon_y)))
        if (int(sensor_y) == target_line):
            sb_on_line.add(sensor_x)
        if (int(beacon_y) == target_line):
            sb_on_line.add(beacon_x)

    return sensors, beacons, len(sb_on_line)

def distance(sensor, beacon):
    # Manhatten Distance dx + dy
    distances = []
    for s,b in zip(sensor, beacon):
        dx = abs(s[0]- b[0])
        dy = abs(s[1]- b[1])
        distances.append(dx+dy)
    return distances

def s_on_y(distances, sensors, target_line):
    soys = []
    for d, s in zip(distances, sensors):
        dys = abs(s[1] - target_line)
        soy = d-dys
        if soy >=0:
            soys.append((s[0],soy))
    return soys

def fill_line(xdists):
    line = []
    for x,d in xdists:
        # fill right
        line.extend([i for i in range(x, x+d+1)])
        # fill left
        line.extend([i for i in range( x-d, x)])

    return set(line)

def result(lines, target_line):
    sensors, beacons, sb_on_line = l2coords(lines, target_line)
    # distance for pairs -> return list of distances
    distances = distance(sensors, beacons)

    dist4 = distances[3]
    sens4 = sensors[3]
    print("dist",cdist([[4,5]], [(3,3)], metric="cityblock"))
    for j, sens in enumerate(sensors):
        print(j, sens)
        for d in trange(distances[j]):
            outerx = sens[0] + d + 1
            outery = sens[1] + distances[j] - d
            for i, sensi in enumerate(sensors):
                if i == j:
                    continue
                if cdist([[outerx,outery]], [sensi], metric="cityblock") > distances[i]:
                    if (i == 31) and (outerx < 4_000_000) and (outery < 4_000_000):
                        print(outerx, outery)
                        print(outerx*4_000_000 + outery)
                        return outerx*4_000_000 + outery
                else:
                    break
            continue

        pass


    res = 0
    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines, target_line=2_000_000)

    print(res)