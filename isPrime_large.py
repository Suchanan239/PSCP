'''isPrime_large'''
def main(num=int(input())):
    '''isPrime_large'''
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
main()
