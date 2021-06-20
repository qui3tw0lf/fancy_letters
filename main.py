import os
import sys
import string
import random

colors_dict = {'RED': '\033[31m', 'GREEN': '\033[32m', 'YELLOW': '\033[33m', 'BLUE': '\033[34m', 'MAGENTA': '\033[35m', 'CYAN': '\033[36m', 'WHITE': '\033[37m', 'ENDC': '\033[0m'}

class bcolors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    ENDC = '\033[0m'

COLORS = ["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"]
LETTER_PATTERNS = {' ': [], '.': []}
for x in string.ascii_uppercase:
	LETTER_PATTERNS[x] = []


def setup_letters():
	LETTER_PATTERNS['.'].append(list('     '))
	LETTER_PATTERNS['.'].append(list('     '))
	LETTER_PATTERNS['.'].append(list('     '))
	LETTER_PATTERNS['.'].append(list('***  '))
	LETTER_PATTERNS['.'].append(list('***  '))

	LETTER_PATTERNS[' '].append(list('     '))
	LETTER_PATTERNS[' '].append(list('     '))
	LETTER_PATTERNS[' '].append(list('     '))
	LETTER_PATTERNS[' '].append(list('     '))
	LETTER_PATTERNS[' '].append(list('     '))

	LETTER_PATTERNS['A'].append(list('*****'))
	LETTER_PATTERNS['A'].append(list('*   *'))
	LETTER_PATTERNS['A'].append(list('*****'))
	LETTER_PATTERNS['A'].append(list('*   *'))
	LETTER_PATTERNS['A'].append(list('*   *'))

	LETTER_PATTERNS['B'].append(list('****'))
	LETTER_PATTERNS['B'].append(list('*   *'))
	LETTER_PATTERNS['B'].append(list('****'))
	LETTER_PATTERNS['B'].append(list('*   *'))
	LETTER_PATTERNS['B'].append(list('****'))

	LETTER_PATTERNS['C'].append(list('*****'))
	LETTER_PATTERNS['C'].append(list('*'))
	LETTER_PATTERNS['C'].append(list('*'))
	LETTER_PATTERNS['C'].append(list('*'))
	LETTER_PATTERNS['C'].append(list('*****'))

	LETTER_PATTERNS['D'].append(list('****'))
	LETTER_PATTERNS['D'].append(list('*   *'))
	LETTER_PATTERNS['D'].append(list('*   *'))
	LETTER_PATTERNS['D'].append(list('*   *'))
	LETTER_PATTERNS['D'].append(list('****'))

	LETTER_PATTERNS['E'].append(list('*****'))
	LETTER_PATTERNS['E'].append(list('*'))
	LETTER_PATTERNS['E'].append(list('***'))
	LETTER_PATTERNS['E'].append(list('*'))
	LETTER_PATTERNS['E'].append(list('*****'))

	LETTER_PATTERNS['F'].append(list('*****'))
	LETTER_PATTERNS['F'].append(list('*'))
	LETTER_PATTERNS['F'].append(list('***'))
	LETTER_PATTERNS['F'].append(list('*'))
	LETTER_PATTERNS['F'].append(list('*'))

	LETTER_PATTERNS['G'].append(list('*****'))
	LETTER_PATTERNS['G'].append(list('*'))
	LETTER_PATTERNS['G'].append(list('*  **'))
	LETTER_PATTERNS['G'].append(list('*   *'))
	LETTER_PATTERNS['G'].append(list('*****'))

	LETTER_PATTERNS['H'].append(list('*   *'))
	LETTER_PATTERNS['H'].append(list('*   *'))
	LETTER_PATTERNS['H'].append(list('*****'))
	LETTER_PATTERNS['H'].append(list('*   *'))
	LETTER_PATTERNS['H'].append(list('*   *'))

	LETTER_PATTERNS['I'].append(list('*****'))
	LETTER_PATTERNS['I'].append(list('  *'))
	LETTER_PATTERNS['I'].append(list('  *'))
	LETTER_PATTERNS['I'].append(list('  *'))
	LETTER_PATTERNS['I'].append(list('*****'))

	LETTER_PATTERNS['J'].append(list('*****'))
	LETTER_PATTERNS['J'].append(list('  *'))
	LETTER_PATTERNS['J'].append(list('  *'))
	LETTER_PATTERNS['J'].append(list('* *'))
	LETTER_PATTERNS['J'].append(list('***'))

	LETTER_PATTERNS['K'].append(list('*   *'))
	LETTER_PATTERNS['K'].append(list('*  *'))
	LETTER_PATTERNS['K'].append(list('**'))
	LETTER_PATTERNS['K'].append(list('* *'))
	LETTER_PATTERNS['K'].append(list('*   *'))

	LETTER_PATTERNS['L'].append(list('*'))
	LETTER_PATTERNS['L'].append(list('*'))
	LETTER_PATTERNS['L'].append(list('*'))
	LETTER_PATTERNS['L'].append(list('*'))
	LETTER_PATTERNS['L'].append(list('*****'))

	LETTER_PATTERNS['M'].append(list('*   *'))
	LETTER_PATTERNS['M'].append(list('* * *'))
	LETTER_PATTERNS['M'].append(list('*   *'))
	LETTER_PATTERNS['M'].append(list('*   *'))
	LETTER_PATTERNS['M'].append(list('*   *'))

	LETTER_PATTERNS['N'].append(list('*   *'))
	LETTER_PATTERNS['N'].append(list('**  *'))
	LETTER_PATTERNS['N'].append(list('* * *'))
	LETTER_PATTERNS['N'].append(list('*  **'))
	LETTER_PATTERNS['N'].append(list('*   *'))

	LETTER_PATTERNS['O'].append(list('*****'))
	LETTER_PATTERNS['O'].append(list('*   *'))
	LETTER_PATTERNS['O'].append(list('*   *'))
	LETTER_PATTERNS['O'].append(list('*   *'))
	LETTER_PATTERNS['O'].append(list('*****'))

	LETTER_PATTERNS['P'].append(list('*****'))
	LETTER_PATTERNS['P'].append(list('*   *'))
	LETTER_PATTERNS['P'].append(list('*****'))
	LETTER_PATTERNS['P'].append(list('*'))
	LETTER_PATTERNS['P'].append(list('*'))

	LETTER_PATTERNS['Q'].append(list('*****'))
	LETTER_PATTERNS['Q'].append(list('*   *'))
	LETTER_PATTERNS['Q'].append(list('*   *'))
	LETTER_PATTERNS['Q'].append(list('*  *'))
	LETTER_PATTERNS['Q'].append(list('*** *'))

	LETTER_PATTERNS['R'].append(list('*****'))
	LETTER_PATTERNS['R'].append(list('*   *'))
	LETTER_PATTERNS['R'].append(list('***'))
	LETTER_PATTERNS['R'].append(list('*  *'))
	LETTER_PATTERNS['R'].append(list('*   *'))

	LETTER_PATTERNS['S'].append(list(' ****'))
	LETTER_PATTERNS['S'].append(list('*'))
	LETTER_PATTERNS['S'].append(list(' ***'))
	LETTER_PATTERNS['S'].append(list('    *'))
	LETTER_PATTERNS['S'].append(list('****'))

	LETTER_PATTERNS['T'].append(list('*****'))
	LETTER_PATTERNS['T'].append(list('  *'))
	LETTER_PATTERNS['T'].append(list('  *'))
	LETTER_PATTERNS['T'].append(list('  *'))
	LETTER_PATTERNS['T'].append(list('  *'))

	LETTER_PATTERNS['U'].append(list('*   *'))
	LETTER_PATTERNS['U'].append(list('*   *'))
	LETTER_PATTERNS['U'].append(list('*   *'))
	LETTER_PATTERNS['U'].append(list('*   *'))
	LETTER_PATTERNS['U'].append(list('*****'))

	LETTER_PATTERNS['V'].append(list('*   *'))
	LETTER_PATTERNS['V'].append(list('*   *'))
	LETTER_PATTERNS['V'].append(list('*   *'))
	LETTER_PATTERNS['V'].append(list(' * *'))
	LETTER_PATTERNS['V'].append(list('  *'))

	LETTER_PATTERNS['W'].append(list('*   *'))
	LETTER_PATTERNS['W'].append(list('*   *'))
	LETTER_PATTERNS['W'].append(list('*   *'))
	LETTER_PATTERNS['W'].append(list('* * *'))
	LETTER_PATTERNS['W'].append(list('*   *'))

	LETTER_PATTERNS['X'].append(list('*   *'))
	LETTER_PATTERNS['X'].append(list(' * *'))
	LETTER_PATTERNS['X'].append(list('  *'))
	LETTER_PATTERNS['X'].append(list(' * *'))
	LETTER_PATTERNS['X'].append(list('*   *'))

	LETTER_PATTERNS['Y'].append(list('*   *'))
	LETTER_PATTERNS['Y'].append(list(' * *'))
	LETTER_PATTERNS['Y'].append(list('  *'))
	LETTER_PATTERNS['Y'].append(list('  *'))
	LETTER_PATTERNS['Y'].append(list('  *'))

	LETTER_PATTERNS['Z'].append(list('*****'))
	LETTER_PATTERNS['Z'].append(list('   *'))
	LETTER_PATTERNS['Z'].append(list('  *'))
	LETTER_PATTERNS['Z'].append(list(' *'))
	LETTER_PATTERNS['Z'].append(list('*****'))

	# print(LETTER_PATTERNS)


def setup_lines(line):
	cols, rows = os.get_terminal_size()
	# print(cols, rows)
	# print(line)
	words = line.split(" ")
	# print(words)
	lines = []
	count = 0
	tmp_line = []
	tmp_size = 0
	for word in words:
		tmp_word_size = len(word) * 5 + 10
		tmp_buffer_size = cols - tmp_size
		# print("Checking", word, tmp_word_size, "-", "size:", tmp_buffer_size)
		if tmp_word_size <= tmp_buffer_size:
			# print("Adding")
			tmp_size += tmp_word_size
			tmp_line.append(word)
		else:
			# print("Creating new line and adding")
			lines.append(tmp_line)
			tmp_line = [word]
			tmp_size = tmp_word_size
	if len(tmp_line):
		lines.append(tmp_line)
	# print(lines)
	for line in lines:
		tmp_line = " ".join(line)
		echo(tmp_line)



def echo(text):
	text = text.upper()
	words = text.split(" ")
	length = len(words)
	colors_list = []
	for x in range(length):
		colors_list.append(random.choice(COLORS))

	for y in range(5):
		count = 0
		for x in text:
			if x == " ":
				count += 1
			if x in LETTER_PATTERNS:
				tmp_letter = "".join(LETTER_PATTERNS[x][y])
				if len(tmp_letter) < 5:
					tmp_letter += " " * (5 - len(tmp_letter))
				print(colors_dict[colors_list[count]], tmp_letter, bcolors.ENDC, sep="", end=" ")
		print()


line = sys.argv[1]
setup_letters()
setup_lines(line)
# echo(line)