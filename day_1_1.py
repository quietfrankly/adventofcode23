import fileinput

total = 0

for line in fileinput.input():
	clean_line = line.strip()
	first_num = None
	last_num = None
	for char in clean_line:
		if char.isdigit():
			if first_num == None:
				first_num = char
				last_num = char
			else:
				last_num = char

	total += int(first_num + last_num)

print(total)
