'''Grade III'''
def main():
    '''Grade III'''
    lines = int(input())
    pts = 0
    gradettl = 0
    for _ in range(lines):
        pts = float(input())
        if pts >= 95:
            gradettl += 4.00
        elif pts >= 90 and pts < 95:
            gradettl += 3.50
        elif pts >= 85 and pts < 90:
            gradettl += 3.00
        elif pts >= 80 and pts < 85:
            gradettl += 2.50
        elif pts >= 75 and pts < 80:
            gradettl += 2.00
        elif pts >= 70 and pts < 75:
            gradettl += 1.50
        elif pts >= 65 and pts < 70:
            gradettl += 1.00
        elif pts >= 60 and pts < 65:
            gradettl += 0.50
        elif pts < 60:
            gradettl += 0.00
    avggrade = gradettl/lines
    avggrade = avggrade*100
    avggrade = int(avggrade)
    avggrade = avggrade/100
    print('%.2f' % avggrade)
main()
