# Functions
def	transpose_list(lst):
	transposed = list()
	i = 0
	max_len = len(max(lst, key=len))
	while i < max_len:
		row = list()
		for item in lst:
			if i < len(item):
				row.append(item[i])
		transposed.append(row)
		i += 1
	return transposed

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip().replace("move ", "").replace("from ", "").replace("to ", "").replace("[", "").replace("] ", "").replace("]", "") for line in file]

crates = lines[:8]
crates = [crate.replace("    ", " ") for crate in crates]
crates =  transpose_list(crates)
for crate in crates:
	while(" " in crate):
		crate.remove(" ")

movements = list()
for movement in lines[10:]:
	mov = movement.split(" ")
	mov[0] = int(mov[0])
	mov[1] = int(mov[1]) - 1
	mov[2] = int(mov[2]) - 1
	movements.append(mov)


crates1 = list() # We need deep copies of crates list, one for exercice
crates2 = list()
i = 0
while i < len(crates):
	crates1.append(crates[i][:])
	crates2.append(crates[i][:])
	i += 1

# Part 1
for movement in movements:
	i = 0
	while i < movement[0]:
		crates1[movement[2]].insert(0, crates1[movement[1]][0])
		crates1[movement[1]].pop(0)
		i += 1

answer1 = str()
for crate in crates1:
	answer1 += crate[0]

print(f"In the top of each stack, the remaining crates are: {answer1}")

# Part 2
for movement in movements:
	to_move = crates2[movement[1]][:movement[0]]
	i = len(to_move) - 1
	while i >= 0:
		crates2[movement[2]].insert(0, to_move[i])
		crates2[movement[1]].pop(0)
		i -= 1

answer2 = str()
for crate in crates2:
	answer2 += crate[0]

print(f"In the top of each stack, the remaining crates are: {answer2}")
