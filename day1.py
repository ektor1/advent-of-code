with open('data/input1.txt', 'r') as file:
    input = file.read()

# Part One
input_arr = input[:-1].split('\n')

col1 = [int(row.split()[0]) for row in input_arr]
col2 = [int(row.split()[1]) for row in input_arr]

col1.sort()
col2.sort()

sum = 0

for val1, val2 in zip(col1, col2):
    sum += abs(val1 - val2)

print(sum)


# Part Two
num_map = {i: 0 for i in col1}
for num in col2:
    if num in num_map:
        num_map[num] += 1

similarity_score = 0
for num, freq in num_map.items():
    similarity_score += num * freq

print(similarity_score)
