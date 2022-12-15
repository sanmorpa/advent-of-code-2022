import math

import tqdm


# Function definitions
def manhattan(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def manhattan_perimeter(a, b):
	perimeter = set()
	distance = manhattan(a,b)
	min_y = a[1] - distance
	if min_y < 0:
		min_y = 0
	elif min_y > 4000000:
		min_y = 4000000

	max_y = a[1] + distance
	if max_y < 0:
		max_y = 0
	elif max_y > 4000000:
		max_y = 4000000
	perimeter.add(tuple([a[0], min_y - 1]))
	perimeter.add(tuple([a[0], min_y + 1]))
	i = 1
	while min_y <= max_y:
		perimeter.add(tuple([a[0] - i - 1, min_y]))
		perimeter.add(tuple([a[0] + i + 1, min_y]))
		if min_y < a[1]:
			i += 1
		else:
			i -= 1
		min_y += 1
	return perimeter

def manhattan_coordiantes(a, b):
	coordinates = set()
	distance = manhattan(a,b)
	min_y = a[1] - distance
	if min_y < 0:
		min_y = 0
	elif min_y > 4000000:
		min_y = 4000000

	max_y = a[1] + distance
	if max_y < 0:
		max_y = 0
	elif max_y > 4000000:
		max_y = 4000000
	i = 1
	j = i - 1
	while min_y <= max_y:
		while j < i + 1:
			coordinates.add(tuple([a[0] - j, min_y]))
		if min_y < a[1]:
			i += 1
		else:
			i -= 1
		min_y += 1
	return coordinates

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip().replace('Sensor at ', '').replace(' closest beacon is at ', '').replace('x=', '').replace('y=', '').replace(' ', '') for line in file]
lines = [line.split(':') for line in lines]
lines =  [[item.split(',') for item in line] for line in lines]
probes = [[[int(n) for n in item] for item in line] for line in lines]


perimeters = list()

with tqdm.tqdm(total=len(probes)) as pbar:
	for probe in probes:
		perimeters.append(manhattan_perimeter(probe[0], probe[1]))
		pbar.update(1)

items = 0
for perimeter in perimeters:
	items += len(perimeter) * len(probes)

with tqdm.tqdm(total=items) as pbar:
	for perimeter in perimeters:
		for coords in perimeter:
			outside = True
			for probe in probes:
				distance_perimeter = manhattan(probe[0], coords)
				distance_beacon = manhattan(probe[0], probe[1])
				if distance_perimeter < distance_beacon:
					outside = False
					break
		pbar.update(len(perimeter))
		if outside == True:
			print(perimeter)

