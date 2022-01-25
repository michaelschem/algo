import math

stack = [1,4,6,8,9,10,22,35,67,89,400,1000,1001,1002,1034]
# stack = [1,2,3]

def bin_search(needle, stack):
	search_len = len(stack)
	left = stack[:math.floor(search_len/2)]
	right = stack[math.floor(search_len/2):]

	# print(left, right)

	if right[0] == needle:
		return True
	elif len(left) == 0:
		return False
	elif needle > left[-1]:
		return bin_search(needle, right)
	else:
		return bin_search(needle, left)

# print(bin_search(999, stack))


def bin_search_help(needle, stack):
	search_len = len(stack)
	left = stack[:math.floor(search_len/2)]
	right = stack[math.floor(search_len/2):]

	if right[0] == needle:
		return True, None
	elif len(left) == 0:
		return False, None
	elif needle > left[-1]:
		return (needle, right)
	else:
		return (needle, left)


def bin_search_it(needle, stack):
	call_stack =  []

	call_stack.append((needle, stack))

	while len(call_stack) > 0:
		call = call_stack.pop()

		needle, stack = bin_search_help(*call)

		if needle == True or needle == False:
			return needle

		call_stack.append((needle, stack))

print(bin_search_it(10, stack))
print(bin_search_it(2, stack))