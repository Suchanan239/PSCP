"""Stamps"""
def main():
    """Stamps"""
    count = int(input())
    aaa = int(input())
    bbb = int(input())
    ccc = int(input())
    ddd = int(input())
    total = 0
    stamp = 0
    for _ in range(count):
        bill = int(input())
        while bill > 0 and stamp >= ccc:
            stamp -= ccc
            bill = max(bill - ddd, 0)
        total += bill
        stamp += bbb * (bill // aaa)
    print(str(total) + '\n' + str(stamp))
main()
