'''Binary'''
def bi_num(bi_number):
    """Binary"""
    result = []
    while bi_number > 0:
        result.append(bi_number % 2)
        bi_number //= 2
    result.reverse()
    return result

def main():
    """Binary"""
    num = int(input())
    if num == 0:
        print(0)
    for ori in bi_num(num):
        print(ori, end='')
main()
