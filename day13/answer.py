from itertools import zip_longest


# Functions definition
def parse_to_list(s, i=0):
	result = []
	while i < len(s):
		if s[i] == '[':
			i, r = parse_to_list(s, i+1)
			if r != ' ':
				result.append(r)
		elif s[i] == ']':
			return i+1, result
		else:
			if s[i] != ' ':
				result.append(s[i])
			i += 1
	return result

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip().replace(',', ' ') for line in file]

lines = [parse_to_list(line) for line in lines]

signals = list()
new_line = list()
for line in lines:
	if len(line) == 0:
		signals.append(new_line)
		new_line = list()
	else:
		new_line.append(line)
signals.append(new_line)

def check_values(s1, s2, pair):
	for signal1, signal2 in zip_longest(s1, s2):
		if signal1 == None and signal2 != None:
			return True
		elif signal2 == None and signal1 != None:
			return False
		if isinstance(signal1, list):
			if isinstance(signal2, list):
				if (len(signal1) == 0 and len(signal2) != 0):
					return True
				elif (len(signal2) == 0 and len(signal1) != 0):
					return False
				elif (len(signal1) != 0 and len(signal2) != 0):
					return check_values(signal1, signal2, pair)
			elif isinstance(signal2, str):
				return check_values(signal1, list(signal2), pair)
		elif isinstance(signal1, str):
			if isinstance(signal2, list):
				return check_values(list(signal1), signal2, pair)
			elif isinstance(signal2, str):
				if int(signal1) < int(signal2):
					return True
				elif int(signal1) > int(signal2):
					return False

total = 0
for pair in range(len(signals)):
	pair1 = signals[pair][0]
	pair2 = signals[pair][1]
	if check_values(pair1, pair2, pair) == True:
		total += (pair + 1)
print(f"The total is {total}")
