import math

import tqdm


# Function definitions
def manhattan(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip().replace('Sensor at ', '').replace(' closest beacon is at ', '').replace('x=', '').replace('y=', '').replace(' ', '') for line in file]

lines = [line.split(':') for line in lines]
lines =  [[item.split(',') for item in line] for line in lines]
probes = [[[int(n) for n in item] for item in line] for line in lines]

# Part 1

min_x = math.inf
max_x = -math.inf
for probe in probes:
	distance = manhattan(probe[0], probe[1])
	if probe[0][0] + distance > max_x:
		max_x = probe[0][0] + distance
	if probe[0][0] - distance < min_x:
		min_x = probe[0][0] - distance

items = (max_x - min_x) * len(probes)

row = set()
with tqdm.tqdm(total=items) as pbar:
	for probe in probes:
		y = 2000000
		x = min_x - 1
		distance = manhattan(probe[0], probe[1])
		while x <= max_x + 1:
			if manhattan(probe[0], [x, y]) <= distance:
				row.add(x)
			x += 1
			pbar.update(1)

for probe in probes:
	if probe[1][1] == 2000000:
		if probe[1][0] in row:
			row.remove(probe[1][0])

print(f'In the row where y=2000000 {len(row)} positions cannot contain a beacon')
