'''Restaurant'''
def main():
    '''Restaurant'''
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    if aaa > 0 and bbb >= aaa and ccc >= 0 \
        and ccc <= 100 and ddd >= 0:
        if aaa < bbb:
            total = (ccc/100)*(aaa+ddd)
            ggg = abs(ddd-total)
            if ddd > total:
                print("No", "%.3f" %ggg)
            elif ddd < total:
                print("Yes", "%.3f" %ggg)
            elif ddd == total:
                print("Yes")
        elif aaa > bbb:
            print("Yes")
        elif aaa == bbb:
            total = (ccc/100)*(aaa)
            total2 = aaa-total
            total3 = (ccc/100)*(aaa+ddd)
            total4 = aaa+ddd-total3
            total5 = abs(total2-total4)
            if total2 > total4:
                print("Yes", "%.3f" %total5)
            elif total2 < total4:
                print("No", "%.3f" %total5)
            elif total2 == total4:
                print("Yes")
main()
