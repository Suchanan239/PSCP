'''Duplicate I'''
def main():
    '''Duplicate I'''
    num_m = int(input())
    num_n = int(input())
    firstgroup = set()
    secoundgroup = set()
    for _ in range(num_m):
        collegain_m = input()
        firstgroup.add(collegain_m)
    for _ in range(num_n):
        collegian_n = input()
        secoundgroup.add(collegian_n)
    total = firstgroup.intersection(secoundgroup)
    newtotal = (sorted((total), reverse=True))
    if total == set():
        print("Nope")
    else:
        for i in newtotal:
            print(i)
main()
