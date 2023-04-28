'''Difference'''
def main():
    '''Difference'''
    nnn = int(input())
    mmm = int(input())
    allmember_a = set()
    allmember_b = set()
    for _ in range(nnn):
        member_a = int(input())
        allmember_a.add(member_a)
    for _ in range(mmm):
        member_b = int(input())
        allmember_b.add(member_b)
    result = allmember_a - allmember_b
    result = sorted(result)
    for i in result:
        print(i, end=" ")
main()
    