with open('data/input2.txt', 'r') as file:
    input = file.read()
input.split('\n')
input = [i.split() for i in input.split('\n')[:-1]]

# Part One
# O(m * n), where m = number of reports and n = average length of each report
def is_safe(report):
    order = False # descending or the same
    if int(report[0]) - int(report[1]) < 0:
        order = True # ascending order
    for num in range(len(report) - 1):
        diff = int(report[num]) - int(report[num + 1])
        if abs(diff) == 0 or abs(diff) > 3 or (diff < 0) != order:
            return False
    return True

def solution(reports):
    safe = 0
    for row in reports:
        if is_safe(row):
            safe += 1
    return safe

solution(input)


# Part Two
def is_safe2(report):
    order = False # descending or the same
    if int(report[0]) - int(report[1]) < 0:
        order = True # ascending order

    for num in range(len(report) - 1):
        diff = int(report[num]) - int(report[num + 1])
        if abs(diff) == 0 or abs(diff) > 3 or (diff < 0) != order:
            return False
    return True

def solution(reports):
    safe = 0

    for row in reports:
        if is_safe2(row):
            safe += 1
        else:
            for index in range(len(row)):
                copy = row.copy()
                copy.pop(index)
                if is_safe2(copy):
                    safe += 1
                    break

    return safe

solution(input)
