# Functions declaration

def	move_directoy(dir, command):
	if command[2] == "/":
		dir = "/"
	elif command[2] == "..":
		check = len(dir) - 2
		while check >= 0 and dir[check] != "/":
			check -= 1
		dir = dir[:(check + 1)]
	else:
		dir += command[2] + "/"
	return dir

# Data ingestion and processing
with open("input.txt") as file:
	lines = [line.rstrip() for line in file]
terminal = [line.split(" ") for line in lines]

# Part 1
folders = dict()
dir = "/"

command = 0
while command < len(terminal):
	if terminal[command][0] == "$":
		if terminal[command][1] == "cd":
			dir = move_directoy(dir, terminal[command])
			command += 1
		else:
			size = 0
			command += 1
			while command < len(terminal) and terminal[command][0] != "$":
				if terminal[command][0] != "dir":
					size += int(terminal[command][0])
				command += 1
			folders[dir] = size

for folder in folders:
	size = folders[folder]
	for fold in folders:
		if folder in fold and folder != fold:
			size += folders[fold]
	folders[folder] = size

total1 = 0
for folder in folders:
	if folders[folder] <= 100000:
		total1 += folders[folder]

print(f"The sum of all the directories with a total size of at most 100000 is {total1}.")

# Part 2
unused = 70000000 - folders["/"]
enough = dict()
for folder in folders:
	if folders[folder] >= (30000000 - unused):
		enough[folder] = folders[folder]

total2 = folders[min(enough, key=enough.get)]
print(f"The directory to free is {min(enough, key=enough.get)} with a total space of {total2}.")
