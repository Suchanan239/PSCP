'''OTP'''
def main():
    '''OTP'''
    while True:
        num = input()
        if num == '0':
            break
        num_count = [num.count(str(i)) for i in range(0, 10)]
        if len(num) == 4 and num_count.count(2) == 1:
            print('Valid')
        elif len(num) == 6 and (num_count.count(2) == 2 or \
            num_count.count(3) == 1):
            print('Valid')
        elif len(num) == 8 and (num_count.count(2) == 3 or \
            num_count.count(3) == 2):
            print('Valid')
        else:
            print('Invalid')
main()
