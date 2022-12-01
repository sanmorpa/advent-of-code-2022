import functools

# part 1

with open("day01.txt") as file:
	lines = [line for line in file]

cleaned = list()
row = list()
for line in lines:
	if line == "\n":
		cleaned.append(row)
		row.clear()
	else:
		row.append(line.replace('\n', ''))

cleaned = [[int(n) for n in row] for row in cleaned]

elf_food = list(map(lambda row: functools.reduce(lambda a, b: a + b, row, 0), cleaned))
print(f"The elf with the most amount of calories has: {max(elf_food)} calories.")

# Part 2

elf_food = sorted(elf_food, reverse=True)
print(f"The top 3 elves with the most amount of calories have: {elf_food[0] + elf_food[1] + elf_food[2]} calories between them.")
