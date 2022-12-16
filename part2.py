data = open('input.txt', 'r').readlines()
data = [i.strip('\n') for i in data]
crates = []
for i in range(len(data)-505):
	for j in range(len(data[i])):
		data[i] = list(data[i])
		if data[i][j] == '[' or data[i][j] == ']':
			data[i][j] = ' '
	crates.append(data[i])

crates = [list(tup) for tup in zip(*crates)]
for i in crates:
	while [' ',' ',' '] in crates:
		crates.remove([' ',' ',' '])
for i in crates:
	while (' ' in i):
		i.remove(' ')

movement = []
for i in data[10:]:
	temp_list = i.split(' ')
	one = int(temp_list[1])
	two = int(temp_list[3])
	three = int(temp_list[5])
	movement.append([one,two,three])
new_crates = [i for i in crates if i != []]

for i in movement:
	amountOfCratesToMove = i[0]
	stackToMoveFrom = i[1]-1
	stackToMoveTo = i[2]-1
	temp = new_crates[stackToMoveFrom][:amountOfCratesToMove]
	for i in temp:
		new_crates[stackToMoveFrom].remove(i)
	new_crates[stackToMoveTo] = temp + new_crates[stackToMoveTo]
answer = []
for i in new_crates:
	answer.append(i[0])
print(answer)