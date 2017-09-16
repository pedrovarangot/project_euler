from itertools import permutations

def domul(n, t):
	res = ''
	for d in t:
		res += str(d*n)
	return int(res)

pandigitals19 = set([int(''.join(d)) for d in permutations('123456789', 9)])

def test():
	for i in range(2,6+1):
		concat = range(1,i+1)
		for j in range(1, 9 // i + 1):
			all_candidates = [int(''.join(d)) for d in permutations('123456789', j)]
			for candidate in all_candidates:
				if domul(int(candidate), concat) in pandigitals19:
					print(int(candidate), concat, domul(int(candidate), concat))