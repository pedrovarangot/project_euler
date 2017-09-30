w1 = 'the'

def test(ctn, k):
    maxrating = 0
    tkey = 'aaa'
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                key = [i,j,k]
                dec = []
                for n in range(len(ctn)):
                    dec.append(ctn[n] ^ key[n % 3])
                decs = ''.join(map(chr, dec)).lower()
                rating =  decs.count(' ') + decs.count('e') + decs.count('the') + decs.count('be')
                if rating > maxrating:
                    maxrating = rating
                    tkey = ''.join(map(chr, key))
    return tkey


k = input().strip()
ctn = list(map(int, input().strip().split()))
print(test(ctn, k))
