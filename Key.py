'''Key'''
def main():
    '''Key'''
    id_num = input()
    id_number = int(id_num[10:13]) * 10
    id_sum = 0
    id_int = 0
    for _ in id_num:
        id_int = int(_)
        id_sum += id_int
    id_key = str(id_sum + id_number)
    if len(id_key) >= 5:
        print(id_key[1:5])
    elif len(id_key) <= 3:
        id_less = int(id_key) + 1000
        print(id_less)
    else:
        print(id_key)
main()
