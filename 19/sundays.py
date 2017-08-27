#/usr/bin/env python3

def leap(y):
    century = y % 100 == 0
    rv = (y % 4 == 0)
    if rv and century:
        rv = y % 400 == 0
    return rv

def first_day_of_year(y):

    years = y - 1899
    return (365*years + (years - 1) // 4 - (years - 1) // 100 +  (years - 1) // 400) % 7

daysofmonth = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
def advance_days_with_leap(y, m):
    rv = 0
    rv += daysofmonth[m]
    if m == 2 and leap(y):
        rv += 1
    return rv


def number_of_first_sundays(y, jd, m):
    first_day = first_day_of_year(y)
    day = 1
    month = m
    rv = 0
    while(day < jd):
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

        