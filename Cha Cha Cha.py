'''Cha Cha Cha'''
def main():
    '''Cha Cha Cha'''
    import math
    days = int(input())
    payment = 0
    for _ in range(1, days+1):
        hours = math.ceil(float(input()))
        total = 8720*hours
        payment = payment + int(total)
    print(payment)
main()
