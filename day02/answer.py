# Data ingestion and processing
with open("input.txt") as file:
	lines = [line.rstrip() for line in file]
games = [row.split() for row in lines]

# part 1
selected = {
	'X': 1, # Rock
	'Y': 2, # Paper
	'Z': 3  # Scissors
}

result = {
	'W': [['C', 'X'], ['A', 'Y'], ['B', 'Z']],
	'L': [['B', 'X'], ['C', 'Y'], ['A', 'Z']],
	'T': [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
}

total1 = 0
for game in games:
	if game in result['W']:
		total1 += 6
	elif game in result['T']:
		total1 += 3
	total1 += selected[game[1]]

print(f"My final result will be: {total1}")


# part 2
expected = {
	'Z': [['C', 'X'], ['A', 'Y'], ['B', 'Z']],
	'X': [['B', 'X'], ['C', 'Y'], ['A', 'Z']],
	'Y': [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
}

total2 = 0
for game in games:
	if game[1] == 'Z':
		total2 += 6
	elif game[1] == 'Y':
		total2 += 3
	for option in expected[game[1]]:
		if game[0] in option:
			total2 += selected[option[1]]

print(f"My final result will be: {total2}")
