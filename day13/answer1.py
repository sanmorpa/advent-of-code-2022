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
lines = [eval(line) for line in lines if len(line) > 0]

signals = list()
new_line = list()
i = 0
for line in lines:
	if i == 2:
		signals.append(new_line)
		new_line = list()
		i = 0
	new_line.append(line)
	i += 1
signals.append(new_line)

#Part 1
total = 0
for pair in range(len(signals)):
	status = check_values(signals[pair][0], signals[pair][1])
	if status == True:
		total += (pair + 1)
print(f"The total of the sorted packets' indexes is {total}")
