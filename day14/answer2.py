import copy
import math


# Function definition
def get_borders(rocks):
	borders = {
		'minX': math.inf,
		'minY': math.inf,
		'maxX': -1,
		'maxY': -1
	}

	for rock in rocks:
		for coordinate in rock:
			if coordinate[0] > borders['maxX']:
				borders['maxX'] = coordinate[0]
			if coordinate[0] < borders['minX']:
				borders['minX'] = coordinate[0]
			if coordinate[1] > borders['maxY']:
				borders['maxY'] = coordinate[1]
			if coordinate[1] < borders['minY']:
				borders['minY'] = coordinate[1]
	return borders

def create_cave(rocks, borders):
	cave = [['.'] * ((borders['maxX'] * 2) + 1) for i in range(borders['maxY'] + 1)]
	for rock in range(len(rocks)):
		x = rocks[rock][0][0]
		y = rocks[rock][0][1]
		for coordinate in range(len(rocks[rock])):
			i = rocks[rock][coordinate][0]
			j = rocks[rock][coordinate][1]
			if i == x:
				if y < j:
					while y <= j:
						cave[y][x] = '#'
						y += 1
					y -= 1
				elif y > j:
					while y >= j:
						cave[y][x] = '#'
						y -= 1
					y += 1
			elif j == y:
				if x < i:
					while x <= i:
						cave[y][x] = '#'
						x += 1
					x -= 1
				elif x > i:
					while x >= i:
						cave[y][x] = '#'
						x -= 1
					x += 1
	return cave

def print_cave(cave, borders):
	for line in range(len(cave)):
			for item in range(len(cave[line])):
				if item >= borders['minX'] and item <= borders['maxX']:
					print(cave[line][item], end='')
			print()

def can_drop(cave, sand):
	if cave[sand[1] + 1][sand[0]] == '.':
		return True
	elif cave[sand[1] + 1][sand[0] - 1] == '.' or cave[sand[1] + 1][sand[0] + 1] == '.':
			return True
	return False

def accumulated_sand(source, cave):
	dropped = 0
	while True:
		sand = list(source)
		cave[0][500] = 'o'
		while can_drop(cave, sand) == True:
			cave[sand[1]][sand[0]] = '.'
			if cave[sand[1] + 1][sand[0]] == '.':
				cave[sand[1] + 1][sand[0]] = 'o'
				sand[1] += 1
			elif cave[sand[1] + 1][sand[0] - 1] == '.':
				cave[sand[1] + 1][sand[0] - 1] = 'o'
				sand[1] += 1
				sand[0] -= 1
			elif cave[sand[1] + 1][sand[0] + 1] == '.':
				cave[sand[1] + 1][sand[0] + 1] = 'o'
				sand[1] += 1
				sand[0] += 1
		if cave[0][500] == 'o':
			return dropped + 1
		dropped += 1

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]

lines = [line.split(' -> ') for line in lines]

rocks = [[item.split(',') for item in line] for line in lines]

rocks = [[[int(coord) for coord in stone] for stone in rock] for rock in rocks]

borders = get_borders(rocks)

cave = create_cave(rocks, borders)
cave.append(['.'] * ((borders['maxX'] * 2) + 1))
cave.append(['#'] * ((borders['maxX'] * 2) + 1))
borders['maxY'] += 2
dropped = accumulated_sand((500, 0), cave)

print(f"The total grains of sand that dropped before reaching the source is {dropped}.")
