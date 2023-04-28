'''SqFree'''
def sqfree(num):
    '''SqFree'''
    if num%2 == 0:
        num /= 2
    if num%2 == 0:
        return False
    for i in range(3, int((num**0.5)+1)):
        if num%i == 0:
            num /= i
        if num%i == 0:
            return False
    return True
def main():
    '''SqFree'''
    result = 0
    for i in range(1, int(input())+1):
        if sqfree(i):
            result += 1
    print(result)
main()
