import functools

# Data ingestion and processing
with open("input.txt") as file:
	lines = [line for line in file]

backpacks = list()
row = list()
for line in lines:
	if line == "\n":
		backpacks.append(row)
		row = list()
	else:
		row.append(line.replace('\n', ''))

backpacks = [[int(n) for n in row] for row in backpacks]

# part 1
elf_food = list(map(lambda row: functools.reduce(lambda a, b: a + b, row, 0), backpacks))
print(f"The elf with the most amount of calories has: {max(elf_food)} calories.")

# Part 2
elf_food = sorted(elf_food, reverse=True)
print(f"The top 3 elves with the most amount of calories have: {elf_food[0] + elf_food[1] + elf_food[2]} calories between them.")
