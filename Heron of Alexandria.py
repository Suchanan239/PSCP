'''Heron of Alexandria'''
def main(aaa=float(input()), bbb=float(input()), ccc=float(input())):
    '''Heron of Alexandria'''
    import math
    sss = (aaa+bbb+ccc)/2
    area = math.sqrt(sss*(sss-aaa)*(sss-bbb)*(sss-ccc))
    print("%.3f" %area)
main()
