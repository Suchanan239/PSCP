'''SMS'''
def main():
    '''SMS'''
    list1 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"],\
         ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"], \
            ["T", "U", "V"], ["W", "X", "Y", "Z"]]
    val = []
    for _ in range(int(input())):
        num_first = int(input())
        num_secound = int(input())
        if num_first == 1:
            for _ in range(num_secound):
                if len(val) > 0:
                    val.pop()
        if num_first == 2 or num_first == 3 \
            or num_first == 4 or num_first == 5 \
                or num_first == 6 or num_first == 8 \
                    and num_secound != 0:
            if num_secound % 3 == 0:
                val.append(list1[num_first-2][2])
            else:
                val.append(list1[num_first-2][(num_secound%3)-1])
        if num_first == 7 or num_first == 9:
            if num_secound % 4 == 0:
                val.append(list1[num_first-2][3])
            else:
                val.append(list1[num_first-2][(num_secound%4)-1])
    if len(val) > 0:
        return print(*val, sep="")
    print("null")
main()
