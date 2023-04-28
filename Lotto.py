"""Lotto"""
def plus_near1(sum1):
    """lotto"""
    result = sum1
    if sum1 < 0:
        result = 1000000+sum1
    result = "%07d"%result
    return str(result)[1:7]
def main():
    """main"""
    lotto_win1 = input()
    lotto_win2 = input()
    lotto_win311 = input()
    lotto_win312 = input()
    lotto_win321 = input()
    lotto_win322 = input()
    my_lotto = input()
    pize = 0
    if my_lotto == lotto_win1:
        pize += 6000000
    if my_lotto[4:6] == lotto_win2:
        pize += 2000
    if my_lotto[0:3] == lotto_win311:
        pize += 4000
    if my_lotto[0:3] == lotto_win312:
        pize += 4000
    if my_lotto[3:6] == lotto_win321:
        pize += 4000
    if my_lotto[3:6] == lotto_win322:
        pize += 4000
    if plus_near1(int(lotto_win1)-1) == my_lotto or \
        plus_near1(int(lotto_win1)+1) == my_lotto:
        pize += 100000
    print(pize)
main()
