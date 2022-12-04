# Data ingestion and processing
with open("input.txt") as file:
	lines = [line.rstrip() for line in file]

pairs = [line.split(",") for line in lines]

pairs = [[task.split("-") for task in pair] for pair in pairs]

# Part 1
total1 = 0
for pair in pairs:
	if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
		total1 += 1
	elif int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
		total1 += 1

print(f"The number of pairs that have complete overlap is: {total1}")

# Part 2

total2 = 0
for pair in pairs:
	if (int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][0])) or (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][0]) <= int(pair[1][1])):
		total2 += 1
	elif (int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][0])) or (int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][0]) <= int(pair[0][1])):
		total2 += 1

print(f"The number of pairs that have at least partial overlap is: {total2}")
# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]
# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]
# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]
# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]
# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]
# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]
# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]
