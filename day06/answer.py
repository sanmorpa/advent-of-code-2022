# Data ingestion and processing
with open('input.txt') as file:
	lines = [line.rstrip() for line in file][0]

count1 = 4
buffer = lines[:count1]
repeated = set(buffer)

while len(buffer) != len(repeated):
	count1 += 1
	buffer = lines[(count1 - 4):count1]
	repeated = set(buffer)
print(f"{count1} characters need to be processed before the first start-of-packet marker is detected")

# part 2

count2 = 14
buffer = lines[:count2]
repeated = set(buffer)

while len(buffer) != len(repeated):
	count2 += 1
	buffer = lines[(count2 - 14):count2]
	repeated = set(buffer)
print(f"{count2} characters need to be processed before the first start-of-packet marker is detected")
