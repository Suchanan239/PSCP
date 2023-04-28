'''Day2011'''
def main():
    '''Day2011'''
    day = int(input())
    month = int(input())
    day_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayofyear = sum(day_of_months[:month-1])+day
    day = dayofyear%7
    if day == 1:
        print("Saturday")
    elif day == 2:
        print("Sunday")
    elif day == 3:
        print("Monday")
    elif day == 4:
        print("Tuesday")
    elif day == 5:
        print("Wednesday")
    elif day == 6:
        print("Thursday")
    else:
        print("Friday")
main()
