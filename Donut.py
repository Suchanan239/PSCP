"""Donut"""
def main():
    """Donut"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    aaa = num4%(num2+num3)
    ddd = num4//(num2+num3)
    if aaa < num2:
        ttt = num1*(num2*ddd+aaa)
        total = ddd*(num2+num3)+aaa
        print(ttt, total)
    else:
        ddd += 1
        ttt = num1*num2*ddd
        total = ddd*(num2+num3)
        print(ttt, total)
main()
