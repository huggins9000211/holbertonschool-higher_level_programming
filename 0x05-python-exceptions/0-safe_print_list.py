#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	counter = 0
	for x in range(0, x):
		try:
			print(my_list[x], end="")
		except IndexError as err:
			pass
		else:
			counter += 1
	print()
	return counter
