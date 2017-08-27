singles = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
tenmults = {20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}
# "Thousand", "Million", "Billion", "Trillion"

def do_twodigs(num):
    if num < 20:
        return singles[num]
    else:
        rv = tenmults[num//10*10]
        if num % 10 > 0:
            rv += " " + singles[num % 10]
        return rv
    return "Error S"

def do_hund(num):
    if num < 100:
        return do_twodigs(num)
    else:
        rv = singles[num // 100] + " Hundred"
        if num - (num // 100 * 100) > 0:
            rv += " and " + do_twodigs(num - (num // 100 * 100))
        return rv
    return "Error H"

res = ""
for i in range(1, 1001):
    num = i
    if num == 0:
        print("Zero")
        continue
    num_str = str(num)
    hunds = ""
    mils = ""
    
    if num >= 1000:
        if int(num_str[len(num_str)-3:]) > 0:
            hunds = " and " + do_hund(int(num_str[len(num_str)-3:]))
        mils = do_hund(num // 1000) + " Thousand "
    else:
        hunds = do_hund(num)
        mils = ""
    print(mils + hunds)
    res += (mils + hunds)
print(len(res.strip().replace(" ", "")))