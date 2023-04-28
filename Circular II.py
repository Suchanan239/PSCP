"""Circular II"""
def main():
    """Circular II"""
    import math
    myx = float(input())
    myy = float(input())
    myr = float(input())
    fdx = float(input())
    fdy = float(input())
    fdr = float(input())
    assumedt = math.sqrt(((myx-fdx)**2)+((myy-fdy)**2))
    realdt = myr+fdr
    total = assumedt - realdt
    if total < 0:
        print("Yes")
    else:
        print("No")
main()
