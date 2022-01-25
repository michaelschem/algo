# Wordl solver

import re

base_reg_in = input("Base reg: ")
valid_letters = input("Valid letters: ")

valid_letters = f"[{valid_letters}]"

base_reg = re.compile("\n" + base_reg_in.replace('.',valid_letters) + "\n")
print(base_reg)

with open("words.txt", 'r') as dictionary:
	for word in base_reg.findall(dictionary.read()):
		print(word)


