'''Inflation'''
def main():
    '''Inflation'''
    money = int(float(input())*100)
    year = int(input())
    if money == 0:
        print('0.00')
    else:
        for _ in range(year):
            money = money + (money*381)//10000
        char_count = len(str(money)) - 2
        print(str(money)[0:char_count]+'.'+(str(money)[char_count:]))
main()
