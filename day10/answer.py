# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]

instructions = [line.split(" ") for line in lines]

cycles = [20, 60, 100, 140, 180, 220]

# Part 1
value = 1
cycle = 1
total1 = 0

for instruction in instructions:
	if cycle in cycles:
		total1 +=  value * cycle
	if instruction[0] == 'addx':
		cycle += 1
		if cycle in cycles:
			total1 +=  value * cycle
		value += int(instruction[1])
	cycle += 1

print(f"The sum of the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles is {total1}\n")

# Part 2
screen = [' '] * 240
values = [1, 2, 3]
draw = 1
pixel = 0

for instruction in instructions:
	if draw in values:
		screen[pixel] = '#'
	if instruction[0] == 'addx':
		draw += 1
		pixel += 1
		if pixel % 40 == 0:
			draw = 1
		if draw in values:
			screen[pixel] = '#'
		values = [value + int(instruction[1]) for value in values]
	draw += 1
	pixel += 1
	if pixel % 40 == 0:
		draw = 1

i = 1
for row in screen: #BRJLFULP
	for pixel in row:
		print(pixel, end="")
		i += 1
		if i == 41:
			print()
			i = 1
