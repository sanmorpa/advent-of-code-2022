import re

# Funtion definitions
def	operation(start, type, n, mod):
	if n == -1:
		n = start
	if type == '*':
		result = start * n
	else:
		result = start + n
	return result % mod

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]

monkeys = [{'items': list(), 'operation': list(),'test': list(), 'inspected': 0} for line in lines if 'Monkey' in line]

lines = [line.split(' ') for line in lines]
lines = [[item.replace(',', '').replace(':', '') for item in line] for line in lines]

for line in range(len(lines)):
	for item in range(len(lines[line])):
		lines[line][item] = re.sub(r'[^?:0-9|\*|+]', '', lines[line][item])

for line in lines:
	while '' in line:
		line.remove('')
while [] in lines:
	lines.remove([])

count = 0
for line in lines:
	if count == 6:
		count = 0
	if count == 0:
		monkey = int(line[0])
	elif count == 1:
		monkeys[monkey]['items'] = [int(item) for item in line]
	elif count == 2:
		monkeys[monkey]['operation'].append(line[0])
		if len(line) > 1: monkeys[monkey]['operation'].append(int(line[1]))
		else: monkeys[monkey]['operation'].append(-1)
	elif count > 2 and count < 6:
		monkeys[monkey]['test'].append(int(line[0]))
	count += 1

total_mods = 1
for monkey in monkeys:
	total_mods *= monkey['test'][0]

i = 0
while i < 10000:
	for monkey in monkeys:
		monkey['inspected'] += len(monkey['items'])
		for item in monkey['items']:
			new = operation(item, monkey['operation'][0], monkey['operation'][1], total_mods)
			if new % monkey['test'][0] == 0:
				monkeys[monkey['test'][1]]['items'].append(new)
			else:
				monkeys[monkey['test'][2]]['items'].append(new)
		monkey['items'] = list()
	i += 1

first = 0
second = 0
for monkey in monkeys:
	print(monkey)
	if monkey['inspected'] > first:
		second = first
		first = monkey['inspected']
	else:
		if monkey['inspected'] > second:
			second = monkey['inspected']
print(first, second, first * second)
