'''LetterFrequency'''
import string
def main():
    '''LetterFrequency'''
    sen = input().lower().replace(" ", "")
    freq = list(filter(lambda a: a in string.ascii_letters, sen))
    freq = max(set(sen), key=sen.count)
    print(freq)
main()
