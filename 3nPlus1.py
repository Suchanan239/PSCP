'''3nPlus1'''
def sequence(num):
    '''3nPlus1'''
    val = []
    while num != 1:
        val.append(num)
        if num%2 == 0:
            num = num//2
        else:
            num = 3*num+1
    val.append(1)
    return len(val)
def main():
    '''3nPlus1'''
    nums = []
    while True:
        val = int(input())
        if val == 0:
            break
        nums.append(val)
    for i in nums:
        print(sequence(i))
main()
