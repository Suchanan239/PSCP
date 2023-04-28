'''WordSequence II'''
def main(word_1=input(), word_2=input()):
    '''WordSequence II'''
    for i in range(0, max(len(word_1), len(word_2))+1):
        print(word_2[:i]+word_1[i:])
main()
