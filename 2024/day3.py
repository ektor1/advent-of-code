with open('data/input3.txt', 'r') as file:
    input = file.read()

import re

def sumOfProducts(memory):
    match = re.findall(r"mul\((\d+(?:,\d+)*)\)", memory)
    sum = 0
    for pair in match:
        first, second = pair.split(',')
        sum += int(first) * int(second)

    return sum

sumOfProducts(input)


# Part Two
def part2SumOfProducts(memory):
    uncorrupted_mul = ""
    # gets the beginning of the string until do()
    uncorrupted_mul += re.findall(r"^(.*?)do\(\)", memory, re.DOTALL)[0]
    # gets parts of the string from do() to don'()
    match = re.findall(r"do\(\)(.*?)don't\(\)", memory, re.DOTALL)
    for part in match:
        uncorrupted_mul += part
    return sumOfProducts(uncorrupted_mul)

part2SumOfProducts(input)
