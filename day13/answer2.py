from itertools import zip_longest


# Function definition
def check_values(s1, s2):
	for signal1, signal2 in zip_longest(s1, s2):
		if signal1 == None and signal2 != None:
			return True
		elif signal2 == None and signal1 != None:
			return False
		if (isinstance(signal1, int) and isinstance(signal2, list)) or (isinstance(signal1, list) and isinstance(signal2, int)):
			if isinstance(signal1, int):
				status = check_values([signal1], signal2)
			else:
				status = check_values(signal1, [signal2])
			if status == True:
				return True
			if status == False:
				return False
		if isinstance(signal1, list) and isinstance(signal2, list):
			if signal1 != signal2:
				if (len(signal1) != 0 and len(signal2) != 0):
					status = check_values(signal1, signal2)
					if status == True:
						return True
					if status == False:
						return False
				elif (len(signal1) == 0 and len(signal2) != 0):
					return True
				elif (len(signal2) == 0 and len(signal1) != 0):
					return False
		if isinstance(signal1, int) and isinstance(signal2, int):
			if signal1 < signal2:
				return True
			elif signal1 > signal2:
				return False

# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file]

signals = [eval(line) for line in lines if len(line) > 0]
signals.append([[2]])
signals.append([[6]])

#Part 2
indexed = dict()
for i in range(len(signals)):
	j = 0
	index = 0
	while j < len(signals):
		if j != i:
			if check_values(signals[i], signals[j]) == False:
				index += 1
		j += 1
	indexed[index] = signals[i]

total = 1
sort = sorted(indexed)
for s in sort:
	if indexed[s] == [[2]] or indexed[s] == [[6]]:
		total *= (s + 1)

print(f'The decoder key for the distress signal is {total}')
