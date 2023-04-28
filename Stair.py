"""Stair"""
def main():
    """main"""
    num_1 = int(input())
    num_2 = int(input())
    count = 0
    result = 0
    for _ in range(num_2):
        num_3 = int(input())
        if num_3 > num_1:
            result = "NO"
        elif count+num_3 <= num_1 and count != 0 and result != "NO":
            count += num_3
        elif count+num_3 > num_1 and count != 0 and result != "NO":
            count = 0
        if num_3 <= num_1 and result != "NO" and count == 0:
            count = num_3
            result += 1
    print(result)
main()
