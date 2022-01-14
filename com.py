def compare(a,b, tolerance):
# 	distance = get_distance(a,b)
# 	return tolerance > distance

# def get_distance(a,b):
	print('---')

	shorter, longer = sorted([a, b], key=len)

	itr_s = iter(shorter)
	itr_l = iter(longer)

	errs = 0
	c_s = next(itr_s, None)
	while True:
		c_l = next(itr_l, None)

		# print(c_s, c_l)

		if c_l == None:
			return True

		if c_s == c_l:
			c_s = next(itr_s, None)
		else:
			errs+= 1
			# print('err', errs)

		if errs > tolerance:
			return False



print(compare('abc', 'abc', 1)) #True
print(compare('abc', 'abcd', 1)) #True
print(compare('abc', 'abdc', 1)) #True
print(compare('abc', 'a', 1)) #False
print(compare('abc', 'ac', 1)) #True
print(compare('abc', 'ac', 1)) #True
print(compare('ab', 'ac', 1)) #True
print(compare('axxxxx', 'ac', 1)) #False
print(compare('add', 'ac', 1)) #False
print(compare('add', 'ac', 2)) #True
print(compare('add', 'ac', 3)) #True