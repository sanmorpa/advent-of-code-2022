import math

import tqdm


#Function definition
def find_adjacent(map, i, j):
	adjacents = list()
	k = i - 1
	if k < 0:
		k = 0
	while k < len(map) and k <= (i + 1):
		if k != i and map[k][j] <= (map[i][j] + 1):
			adjacents.append([k, j])
		k += 1
	l = j - 1
	if l < 0:
		l = 0
	while l < len(map[i]) and l <= (j + 1):
		if l != j and map[i][l] <= (map[i][j] + 1):
			adjacents.append([i, l])
		l += 1
	return adjacents

def select_adjacent(nodes, i, j):
	for node in range(len(nodes)):
		if nodes[node]['visited'] == False and nodes[node]['coord']['x'] == j and nodes[node]['coord']['y'] == i:
			return node
	return -1

def find_smallest(nodes):
	size = math.inf
	smallest = -1
	for node in range(len(nodes)):
		if nodes[node]['visited'] == False and nodes[node]['distance'] < size:
			size = nodes[node]['distance']
			smallest = node
	return smallest

def in_path(to_print, i, j):
	for item in to_print:
		if item['coord']['y'] == i and item['coord']['x'] == j:
			return True
	return False

def printing(map, to_print, start):
	for line in range(len(map)):
		for item in range(len(map[line])):
			if line == start[1] and item == start[0]:
				prints = 'S'
			elif line == end[1] and item == end[0]:
				prints = 'E'
			else:
				prints = chr(map[line][item] + 96)
			if in_path(to_print, line, item) == True:
				print(f"\033[92m{prints}\033[0m", end=" ")
			else:
				print(f"{prints}", end=" ")
		print()

def all_visited(nodes):
	for node in nodes:
		if node['visited'] == False:
			return False
	return True

def dijkstra(nodes, now):
	added = -3
	with tqdm.tqdm(total=4138) as pbar:
		while all_visited(nodes) == False:
			for node in now['adjacent']:
				i = select_adjacent(nodes, node[0], node[1])
				if i > -1:
					if nodes[i]['distance'] > (now['distance'] + 1):
						nodes[i]['distance'] = now['distance'] + 1
						nodes[i]['previous'] = nodes.index(now)
			nodes[nodes.index(now)]['visited'] = True
			small = find_smallest(nodes)
			if small == -1:
				break
			now = nodes[small]
			pbar.update(1)
		return nodes

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]

map = [[ord(item) - 96 if item.islower() else item for item in line] for line in lines]

start = list()
end = list()
for line in range(len(map)):
	for item in range(len(map[line])):
		if map[line][item] == 'S':
			start.append(item)
			start.append(line)
			map[line][item] = 1
		elif map[line][item] == 'E':
			end.append(item)
			end.append(line)
			map[line][item] = 26

nodes = list()

for i in range(len(map)):
	for j in range(len(map[i])):
		node = dict()
		if i == start[1] and j == start[0]:
			node['distance'] = 0
		else:
			node['distance'] = math.inf
		node['coord'] = {'x': j, 'y': i}
		node['visited'] = False
		node['adjacent'] = find_adjacent(map, i , j)
		node['previous'] = None
		nodes.append(node)

for node in range(len(nodes)):
	if nodes[node]['distance'] == 0:
		now = nodes[node]
		break

nodes = dijkstra(nodes, now)

final = None
for node in nodes:
	if node['coord']['y'] == end[1] and node['coord']['x'] == end[0]:
		final = node
		break

to_print = [final]
while final['previous'] != None:
	final = nodes[final['previous']]
	to_print.append(final)
to_print.append(final)

j = -1 # Minus one to substract the ending node
for line in range(len(map)):
	for item in range(len(map[line])):
		if in_path(to_print, line, item) == True:
			j += 1

# To see the final map with the path in a graphical way, uncomment the following function call:
# printing(map, to_print, start)

print(f'The minimum amount of steps is {j}')
