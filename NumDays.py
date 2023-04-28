'''NumDays'''
def add(month):
    '''NumDays'''
    days = 0
    for i in range(1, month):
        if i == 2:
            days += 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            days += 30
        else:
            days += 31
    return days

def main():
    '''NumDays'''
    day1, mon1, day2, mon2 = int(input()), int(input()), int(input()), int(input())
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (day1 > year[mon1-1]) or (day2 > year[mon2-1]):
        print("Impossible")
    else:
        days1 = add(mon1)+day1
        days2 = add(mon2)+day2
        print(abs(days1-days2))
main()
