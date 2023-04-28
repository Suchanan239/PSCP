"""RemoveTag"""
def main():
    '''Removetag'''
    text = input()
    lss = text.count("<")
    for _ in range(lss):
        text = text[:text.find("<")] + " " \
            + text[text.find(">")+1:]
    result = text.split()
    print(result)
main()
