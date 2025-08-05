with open("input-day1.txt", "r") as file:
    data = file.read()

def floor_finder(directions):
    directions_map = {"(": 1, ")": -1}

    floor = 0
    for dr in directions:
        floor += directions_map[dr]

    return floor

def basement_finder(directions):
    directions_map = {"(": 1, ")": -1}

    floor = 0
    for i in range(len(directions)):
        floor += directions_map[directions[i]]

        if floor < 0:
            break

    return i + 1

print(basement_finder(data))
