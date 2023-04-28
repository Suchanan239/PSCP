'''FOR!F-Ball'''
def main():
    '''FOR!F-Ball'''
    ball = '1'
    sequence = input()
    for match in sequence:
        if match == 'A' and ball == '1':
            ball = '2'
        elif match == 'C' and ball == '1':
            ball = '3'
        elif match == 'B' and ball == '3':
            ball = '2'
        elif match == 'B' and ball == '2':
            ball = '3'
        elif match == 'C' and ball == '3':
            ball = '1'
        elif match == 'A' and ball == '2':
            ball = '1'
    print(ball)
main()
