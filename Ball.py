"""Ball"""
def main():
    '''Ball'''
    high = float(input())
    times = 0
    ball = (3/5)*high
    while ball > 0.01:
        times += 1
        ball = (3/5)*ball
    print(times)
main()
