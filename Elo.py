'''Elo'''
def main():
    '''Elo'''
    r_a = int(input())
    r_b = int(input())
    s_g = input()
    eaa = 1/(1+(10**((r_b-r_a)/400)))
    ebb = 1/(1+(10**((r_a-r_b)/400)))
    if r_a >= 0 and r_b >= 0:
        if s_g == 'A':
            print("%.2f" %eaa)
        elif s_g == 'B':
            print("%.2f" %ebb)
main()
