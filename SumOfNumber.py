'''SumOfNumber'''
def main():
    '''SumOfNumber'''
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 < num2:
        num1, num2 = num2, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num1 < num3:
        num1, num3 = num3, num1
    if num1 < num2:
        num1, num2 = num2, num1
    print(num1, num2, num3, sep="")
main()
