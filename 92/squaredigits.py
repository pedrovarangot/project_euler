def addsquares(n):
	digits = list(str(n))
	return sum(map(lambda n: n*n, map(int, digits)))

in89 = set()
in1 = set()

def endsin89(n):
	if n in in89:
		return True
	if n in in1:
		return False
	seen1 = 0
	seen89 = 0
	orign = n
	while seen89 < 2:
		n = addsquares(n)
		if n in in89:
			in89.add(orign)
			return True
		if n in in1:
			in1.add(orign)
			return False
		if n == 89:
			seen89 += 1
		if n == 1:
			in1.add(orign)
			return False
	in89.add(orign)
	return True

def test(n):
	numbers_ending_in_89 = 0
	for i in range(1,n):
		if endsin89(i):
			numbers_ending_in_89 += 1

	return numbers_ending_in_89
