'''All_Primes'''
def main(num=int(input()), primes=0):
    '''All_Primes'''
    for i in range(1, num+1):
        if  i > 1:
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                primes += 1
    print(primes)
main()
