'''GCD_v1'''
def main(gcd=int(input()), num=int(input())):
    '''GCD_v1'''
    for i in range(100000, 0, -1):
        if gcd%i == 0 and num%i == 0:
            print(i)
            break
main()
