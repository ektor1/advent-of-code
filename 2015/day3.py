with open("input-day3.txt", "r") as file:
    directions = file.read()


def get_next_coordinate(cur_pos, next_dir):
    if next_dir == "^":
        return (cur_pos[0] + 1, cur_pos[1])
    
    if next_dir == "v":
        return (cur_pos[0] - 1, cur_pos[1])

    if next_dir == ">":
        return (cur_pos[0], cur_pos[1] + 1)

    if next_dir == "<":
        return (cur_pos[0], cur_pos[1] - 1)
    

def unique_houses(directions):
    visited = set()
    cur_pos = (0, 0)

    for d in directions:
        cur_pos = get_next_coordinate(cur_pos, d)
        visited.add(cur_pos)

    return len(visited)


def robo_unique_houses(directions):
    visited = set()
    visited.add((0, 0))
    santa_pos = (0, 0)
    robo_santa_pos = (0, 0)
    robo = False 
    
    for d in directions:
        if robo:
            robo_santa_pos = get_next_coordinate(robo_santa_pos, d)
            visited.add(robo_santa_pos)
            robo = False
        else:
            santa_pos = get_next_coordinate(santa_pos, d)
            visited.add(santa_pos)
            robo = True

    return len(visited)
