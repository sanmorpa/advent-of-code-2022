from functools import reduce

def	add_values(a, b):
	if b.isupper():
		a += ord(b) - 38
		return a
	else:
		a += ord(b) - 96
		return a


# Data ingestion and processing
with open("input.txt") as file:
	lines = [line.rstrip() for line in file]

rucksacks = [(line[:int(len(line) / 2)], line[int(len(line) / 2):]) for line in lines]

# Part 1
doubles = list()
for rucksack in rucksacks:
	for item in rucksack[0]:
		if item in rucksack[1]:
			doubles.append(item)
			break

total1 = reduce(add_values, doubles,0)
print(f"The total priority of all repeated items is: {total1}")

# Part 2
grouped = list()
group = list()
j = 0

for i in range(len(lines)):
	if j == 3:
		j = 0
		grouped.append(group)
		group = list()
	group.append(set(lines[i]))
	j += 1
grouped.append(group)

doubles = list()
for team in grouped:
	for backpack in team:
		for item in backpack:
			if item in team[0] and item in team[1] and item in team[2]:
				doubles.append(item)
				break
			else:
				continue
		break

total2 = reduce(add_values, doubles, 0)
print(f"The total priority of all repeated items by group is: {total2}")
