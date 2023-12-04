import fileinput

total = 0

digit_strings = [
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
]

digit_map = {
	"zero": '0',
	"one": '1',
	"two": '2',
	"three": '3',
	"four": '4',
	"five": '5',
	"six": '6',
	"seven": '7',
	"eight": '8',
	"nine": '9',
}

for line in fileinput.input():
    clean_line = line.strip()
    first_num = None
    last_num = None
    for i in range(len(clean_line)):
        char = clean_line[i]
        if char.isdigit():
            if first_num == None:
                first_num = char
                last_num = char
            else:
                last_num = char
        else:
            potential_digit = clean_line[i:]
            for digit in digit_strings:
                if potential_digit.startswith(digit):
                    if first_num == None:
                        first_num = digit_map[digit]
                        last_num = digit_map[digit]
                    else:
                        last_num = digit_map[digit]		

    total += int(first_num + last_num)

print(total)
