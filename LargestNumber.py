'''LargestNumber'''
def main():
    '''LargestNumber'''
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = str(num1)+str(num2)+str(num3)
    num5 = str(num2)+str(num1)+str(num3)
    num6 = str(num3)+str(num1)+str(num2)
    num7 = str(num3)+str(num2)+str(num1)
    num8 = str(num2)+str(num3)+str(num1)
    num9 = str(num1)+str(num3)+str(num2)
    num4 = int(num4)
    num5 = int(num5)
    num6 = int(num6)
    num7 = int(num7)
    num8 = int(num8)
    num9 = int(num9)
    ddd = largest(num4, largest(num5, largest(num6, largest(num7, largest(num8, num9)))))
    print(ddd)
def largest(ddd1, ddd2):
    """bbb"""
    if ddd1 > ddd2:
        return ddd1
    return ddd2
main()
    