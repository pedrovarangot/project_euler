def ispali(n):
    n = str(n)
    if len(n) % 2 == 0:
        return list(n[:len(n)//2]) == list(reversed(n[len(n)//2:]))
    else:
        return list(n[:len(n)//2]) == list(reversed(n[len(n)//2+1:]))

lychrels = set()
def is_lychrel(n, maxits = 50):

    if maxits == 0:
        return True
    nrev = int(''.join(reversed(str(n))))
    if ispali(n + nrev):
        return False
    else:
        return is_lychrel(n + nrev, maxits - 1)

def test(n):
    total = 0
    for i in range(1, n+1):
        if is_lychrel(i):
            total += 1
    return total