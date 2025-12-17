def part_one(data):
    curr = 50
    zero_p = 0

    for rotation in data:
        direction = rotation[0]
        steps = int(rotation[1:])

        if direction == "R":
            curr += steps
            while curr > 99:
                curr -= 100        
        else:
            curr -= steps
            while curr < 0:
                curr += 100
        
        if curr == 0:
            zero_p += 1

    return zero_p


def part_two(data):
    curr = 50
    zero_passes = 0

    for rotation in data:
        skip_last_check = False
        direction = rotation[0]
        steps = int(rotation[1:])

        if direction == "R":
            curr += steps
            while curr > 99:
                curr -= 100
                zero_passes += 1
                if curr == 0:
                    skip_last_check = True
        
        else:
            if curr == 0:
                zero_passes -= 1
            curr -= steps
            while curr < 0:
                curr += 100
                zero_passes += 1

        if curr == 0 and skip_last_check == False:
            zero_passes += 1

    return zero_passes
