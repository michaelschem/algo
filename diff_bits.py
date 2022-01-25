# provide a function that for f(x,y) returns the difference of binary bits

def bit_dif(x,y):
	x_arr = int_to_bin_arry(x)
	y_arr = int_to_bin_arry(y)

	diffs = 0

	for i in range(0,len(x_arr)):
		if x_arr[i] != y_arr[i]:
			diffs += 1

	return diffs

def int_to_bin_arry(x):
	bin_array = [0] * 20

	for i in range(0, x):
		carry = 1
		pos = 0
		while carry > 0:
			if bin_array[pos] == 0:
				bin_array[pos] = 1
				carry = 0
			else:
				bin_array[pos] = 0
				pos += 1

	return bin_array


x = 1
y = 4
print(int_to_bin_arry(x))
print(int_to_bin_arry(y))

print(bit_dif(x,y))

def multi_bin_diff(*args):
	total = 0
	for i in range(0, len(args)):
		for j in range(i, len(args)):
			print(args[i], args[j], bit_dif(args[i], args[j]))
			total += bit_dif(args[i], args[j])

	return total

print(multi_bin_diff(1,3,5))