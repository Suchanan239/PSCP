'''Hamming'''
def main(count=0):
    '''Hamming'''
    text1 = list(input())
    text2 = list(input())
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            count += 1
    print(count)
main()
