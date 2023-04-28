'''Century'''
import math
def main():
    '''Century'''
    years = int(input())
    for _ in range(years):
        year = input()
        century = year[:4]
        want = int(year[5:])
        if century == 'B.E.':
            year = want - 543
            if year < 1:
                print('ERROR')
            elif year >= 1 and year <= 100:
                print("1")
            else:
                result = math.ceil(year/100)
                print(result)
        elif century == 'A.D.':
            if want < 1:
                print("ERROR")
            elif want >= 1 and want <= 100:
                print("1")
            else:
                result = math.ceil(want/100)
                print(result)
main()
