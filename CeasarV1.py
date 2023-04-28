'''CeasarV1'''
import string

def ceasar(data, shifted):
    """CaesarV1"""
    result = ""
    for i in data:
        if i in string.ascii_letters:
            if i.isupper():
                alp_index = ord(i)-ord('A')
                new_index = (alp_index+shifted)%26
                coded = new_index+ord('A')
                new_alp = chr(coded)
                result = result+new_alp
            else:
                if i != " ":
                    alp_index = ord(i)-ord('a')
                    new_index = (alp_index+shifted)%26
                    coded = new_index+ord('a')
                    new_alp = chr(coded)
                    result = result+new_alp
                else:
                    result += i
        else:
            result += i
    return result

def main():
    """CaesarV1"""
    kyw = int(input())
    word = input()
    result = ceasar(word, kyw)
    print(result)
main()
