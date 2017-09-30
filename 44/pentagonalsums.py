from itertools import combinations
import math

def is_square(n):
	nsqrt = math.sqrt(n)
	return nsqrt == math.ceil(nsqrt), int(nsqrt)

def discriminant(a, b, c):
	return b**2 - 4*a*c

def isqrt(n):

	x = n
	y = (2 ** ((n.bit_length()+1) // 2)) - 1

	while y < x:
		x = y
		y = (x + n // x) // 2
	return x

def is_square_2(n):
	MAXF = 100000000

	if n < MAXF:
		return is_square(n)
	else:
		sqrtn = isqrt(n)
		return sqrtn**2 == n, sqrtn

def is_pentagonal(n):
	sqres = is_square_2(discriminant(3, -1, -n * 2))
	return solves_cuadratic_in_ints(sqres, -1, 3)

def solves_cuadratic_in_ints(sqres, b, a):
	if sqres[0]:
		if (-b + sqres[1]) % (2*a) == 0 and -b + sqres[1] > 0:
			return True
		if (-b - sqres[1]) % (2*a) == 0 and -b - sqres[1] > 0:
			return True

	return False

pentagonal_numbers = [n*(3*n-1) // 2 for n in range(1,1000000)]
#pentagonal_tuples = combinations(pentagonal_numbers, 2)
def test():
	for t in pentagonal_tuples:
		if is_pentagonal(sum(t)) and is_pentagonal(t[1] - t[0]):
			print(t)

def test2():
	n, k = map(int, input().strip().split())
	for i in range(k, n):
		if is_pentagonal(pentagonal_numbers[i] + pentagonal_numbers[i - k]) or\
			is_pentagonal(pentagonal_numbers[i] - pentagonal_numbers[i - k]):
			print(pentagonal_numbers[i])

