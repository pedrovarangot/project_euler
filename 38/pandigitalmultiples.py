from itertools import permutations

def domul(n, t):
	res = ''
	for d in t:
		res += str(d*n)
	return int(res)

pandigitals19 = set([int(''.join(d)) for d in permutations('123456789', 9)])
pandigitals18 = set([int(''.join(d)) for d in permutations('12345678', 8)])

def test9(n):
	res = []
	for i in range(2,6+1):
		concat = range(1,i+1)
		for j in range(1, 9 // i + 1):
			all_candidates = [int(''.join(d)) for d in permutations('123456789', j)]
			for candidate in all_candidates:
				candidate = int(candidate)
				mult = domul(candidate, concat)
				if candidate < n and mult in pandigitals19:
					res.append(candidate)
					#print(int(candidate), concat, domul(int(candidate), concat))
	return res

def test8(n):
	res = []
	for i in range(2,6+1):
		concat = range(1,i+1)
		for j in range(1, 9 // i + 1):
			all_candidates = [int(''.join(d)) for d in permutations('12345678', j)]
			for candidate in all_candidates:
				#print(candidate)
				candidate = int(candidate)
				mult = domul(candidate, concat)
				if candidate < n and mult in pandigitals18:
					res.append(candidate)
					#print(int(candidate), concat, domul(int(candidate), concat))
	return res

def test():
	n, k = map(int, input().strip().split())
	if k == 9:
		r = sorted(test9(n))
	else:
		r = sorted(test8(n))
	for i in r:
		print(i)
