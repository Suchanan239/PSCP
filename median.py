'''Median'''
def median(value):
    '''Median'''
    count = len(value)
    sort = sorted(value)
    return (sort[count//2-1]/2.0+sort[count//2]/2.0, sort[count//2])[count%2]if count else None
def main():
    '''Median'''
    nums = int(input())
    lst = []
    for _ in range(nums):
        number = int(input())
        lst.append(number)
    print("%.1f" %median(lst))
main()