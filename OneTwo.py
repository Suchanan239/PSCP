'''OneTwo'''
def one_two(num):
    '''OneTwo'''
    if num == 1:
        return "1"
    elif num == 2:
        return "2"
    else:
        return one_two(num-1)+one_two(num-2)
def main():
    '''OneTwo'''
    print(one_two(int(input())))
main()
