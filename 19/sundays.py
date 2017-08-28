#/usr/bin/env python3

def leap(y):
    century = y % 100 == 0
    rv = (y % 4 == 0)
    if rv and century:
        rv = y % 400 == 0
    return rv

def first_day_of_year(y):
    y = y - 1
    K = y % 100
    J = y // 100
    return ((1 + 13*14//5 + K + K//4 + J//4 + 5*J) + 6) % 7

daysofmonth = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
def advance_days_with_leap(y, m):
    rv = 0
    rv += daysofmonth[m]
    if m == 2 and leap(y):
        rv += 1
    return rv


def number_of_first_sundays(y, jd, m):
    first_day = first_day_of_year(y)
    day = number_day_of_year(y, m, 1)
    month = m
    rv = 0
    while(day <= jd):
        print("first of {} is {}".format(month, first_day))
        if first_day == 0:
            rv += 1
        jump = advance_days_with_leap(y,month)
        month += 1
        day += jump
        first_day += jump
        first_day = first_day % 7
    return rv
        
def number_day_of_year(y, m, d):
    day = d
    m -= 1
    while m > 0:
        day += advance_days_with_leap(y, m)
        m -= 1
    return day

def test():
    total = 0
    for i in range(2000, 2020):
        total += number_of_first_sundays(i, number_day_of_year(i, 12, 31), 1)
    return total