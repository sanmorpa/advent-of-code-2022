from functools import reduce

# Function definitions
def	transpose_matrix(matrix):
	transposed = []
	for i in range(len(matrix[0])):
		transposed.append(list())
	for n in matrix:
		iter = 0
		for item in n:
			transposed[iter].append(item)
			iter += 1
	return transposed

def check_line(line, seen):
	seen[0] = 1
	height = line[0]
	i = 1
	while i < len(line):
		if line[i] > height:
			if seen[i] == 0:
				seen[i] = 1
			height = line[i]
		i += 1
	i -= 1
	seen[i] = 1
	height = line[i]
	while i >= 0:
		if line[i] > height:
			if seen[i] == 0:
				seen[i] = 1
			height = line[i]
		i -= 1
	return seen

def	scenic_score(map, i, j):
	if i == 0 or i == (len(map) - 1):
		return 0
	if j == 0 or j == (len(map[i]) - 1):
		return 0

	score = list()

	count = 0
	k = i + 1
	while k < len(map) and map[k][j] < map[i][j]:
		count += 1
		k += 1
	if (k < len(map)):
		count += 1
	score.append(count)

	count = 0
	k = i - 1
	while k >= 0 and map[k][j] < map[i][j]:
		count += 1
		k -= 1
	if (k >= 0):
		count += 1
	score.append(count)

	count = 0
	l = j + 1
	while l < len(map[i]) and map[i][l] < map[i][j]:
		count += 1
		l += 1
	if (l < len(map[i])):
		count += 1
	score.append(count)

	count = 0
	l = j - 1
	while l >= 0 and map[i][l] < map[i][j]:
		count += 1
		l -= 1
	if (l >= 0):
		count += 1
	score.append(count)

	return reduce((lambda x, y: x * y), score)

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]

map = [[int(i) for i in line] for line in lines]
seen = [[0] * len(line) for line in lines]

# Part 1
for line in range(len(map)):
	seen[line] = check_line(map[line], seen[line])

transposed_map = transpose_matrix(map)
seen = transpose_matrix(seen)

for line in range(len(transposed_map)):
	seen[line] = check_line(transposed_map[line], seen[line])

answer1 = 0
for line in seen:
	for tree in line:
		if tree == 1:
			answer1 += 1

print(f"The total trees that are visible from outside the grid are {answer1}")


# Part 2
scenic = [[0] * len(line) for line in lines]
for i in range(len(map) - 1):
	for j in range(len(map[i]) - 1):
		scenic[i][j] = scenic_score(map,i, j)

print(f"The highest scenic score possible for any tree is {max([max(line) for line in scenic])}")

