'''RockPaperScissor'''
def main():
    '''RockPaperScissor'''
    aaa = 0
    bbb = 0
    cmpt = input()
    num = len(cmpt)
    for i in range(0, num+1, 2):
        num2 = cmpt[i:i+2]
        if num2 == 'RP':
            bbb += 1
        elif num2 == 'PS':
            bbb += 1
        elif num2 == 'SR':
            bbb += 1
        elif num2 == 'PR':
            aaa += 1
        elif num2 == 'SP':
            aaa += 1
        elif num2 == 'RS':
            aaa += 1
    if aaa == bbb:
        print("DRAW", aaa)
    elif aaa > bbb:
        print("A win ", aaa, "-", bbb, sep="")
    elif aaa < bbb:
        print("B win ", bbb, "-", aaa, sep="")
main()
