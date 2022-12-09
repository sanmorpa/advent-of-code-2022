# Function definitions

def	adjacent(head, tail):
	if head['x'] == tail['x'] and head['y'] == tail['y']: # Same coordinate
		return True
	elif head['y'] == tail['y'] and (head['x'] == (tail['x'] - 1) or head['x'] == (tail['x'] + 1)): # Right-left
		return True
	elif head['x'] == tail['x'] and (head['y'] == (tail['y'] - 1) or head['y'] == (tail['y'] + 1)): # Up-down
		return True
	elif (head['x'] == (tail['x'] + 1) or head['x'] == (tail['x'] - 1)) and (head['y'] == (tail['y'] - 1) or head['y'] == (tail['y'] + 1)): # Diagonals
		return True
	else:
		return False

def	move_tail(head, tail):
	if head['x'] == tail['x']: # Moves vertically
		if head['y'] > tail['y']:
			tail['y'] += 1
		else:
			tail['y'] -= 1
	elif head['y'] == tail['y']: # Moves horizontally
		if head['x'] > tail['x']:
			tail['x'] += 1
		else:
			tail['x'] -= 1
	else: # Moves diagonally
		if head['y'] > tail['y']:
			tail['y'] += 1
		else:
			tail['y'] -= 1
		if head['x'] > tail['x']:
			tail['x'] += 1
		else:
			tail['x'] -= 1
	return tail

def	move_head(head, dir):
	if dir == 'R':
		head['x'] += 1
	elif dir == 'L':
		head['x'] -= 1
	elif dir == 'U':
		head['y'] -= 1
	else:
		head['y'] += 1
	return head

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]

movements = [line.split(" ") for line in lines]

seen = [[0] * 500 for i in range(500)]

head = {
	'x': 249,
	'y': 249
}

tail = [{'x': 249,'y': 249}, {'x': 249,'y': 249}, {'x': 249,'y': 249}, {'x': 249,'y': 249},
{'x': 249,'y': 249}, {'x': 249,'y': 249}, {'x': 249,'y': 249}, {'x': 249,'y': 249},
{'x': 249,'y': 249}]

seen[tail[8]['y']][tail[8]['x']] += 1

for movement in movements:
	dir = movement[0]
	steps = int(movement[1])
	done = 0
	while done < steps:
		tails = 1
		head = move_head(head, dir)
		if adjacent(head, tail[0]) == False:
			tail[0] = move_tail(head, tail[0])
		while tails < 9:
			if adjacent(tail[tails - 1], tail[tails]) == False:
				tail[tails] = move_tail(tail[tails - 1], tail[tails])
			tails += 1
		seen[tail[8]['y']][tail[8]['x']] += 1
		done += 1

total = 0
for row in seen:
	for item in row:
		if item > 0:
			total += 1
print(f"The tail of the rope visit at least once {total} positions")
