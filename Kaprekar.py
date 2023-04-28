'''Kaprekar'''
def main():
    '''Kaprekar'''
    num, count, out = input(), 0, 0
    ordered = reorder_num(num)
    while out != 6174:
        low = int(ordered[0]+ordered[1]+ordered[2]+ordered[3])
        high = int(ordered[3]+ordered[2]+ordered[1]+ordered[0])
        out = high - low
        ordered = reorder_num(str(out).zfill(4))
        count += 1
    print(count)
def reorder_num(num):
    '''Kaprekar'''
    num_a, num_b, num_c, num_d = int(num[0]), int(num[1]), int(num[2]), int(num[3])
    if num_a > num_b:
        num_a, num_b = num_b, num_a
    if num_c > num_d:
        num_c, num_d = num_d, num_c
    if num_a > num_c:
        num_a, num_c = num_c, num_a
    if num_b > num_d:
        num_b, num_d = num_d, num_b
    if num_b > num_c:
        num_b, num_c = num_c, num_b
    return str(num_a), str(num_b), str(num_c), str(num_d)
main()
