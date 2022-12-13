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

#for line in signals:
#	print(line[0])
#	print(line[1])
#	print('     --------         ')

def check_values(s1, s2):
	print(f"S1: {s1}\nS2: {s2}\n")
	for signal1, signal2 in zip_longest(s1, s2):
		print(f"Signal1: {signal1}\nSignal2: {signal2}\n")
		if signal1 == None and signal2 != None:
			return True
		elif signal2 == None and signal1 != None:
			return False
		if isinstance(signal1, list):
			if isinstance(signal2, list):
				if signal1 != signal2:
					if (len(signal1) == 0 and len(signal2) != 0):
						return True
					elif (len(signal2) == 0 and len(signal1) != 0):
						return False
					elif (len(signal1) != 0 and len(signal2) != 0):
						return check_values(signal1, signal2)
			elif isinstance(signal2, str):
				lst_signal = list(signal2)
				if lst_signal != signal1:
					return check_values(signal1, list(signal2))
		elif isinstance(signal1, str):
			if isinstance(signal2, list):
				lst_signal = list(signal1)
				if lst_signal != signal2:
					return check_values(list(signal1), signal2)
			elif isinstance(signal2, str):
				if int(signal1) < int(signal2):
					return True
				elif int(signal1) > int(signal2):
					return False

total = 0
for pair in range(len(signals)):
	pair1 = signals[pair][0]
	pair2 = signals[pair][1]
	if check_values(pair1, pair2) == True:
		print("True")
		total += (pair + 1)
	else:
		print("False")
	print()
print(f"The total is {total}")
