'''HorizontalHistogram'''
def value_sort(num):
    '''HorizontalHistogram'''
    char = num[0]
    return ord(char) + (100 if char.isupper() else 0)

def main(alp):
    '''HorizontalHistogram'''
    for char, count in sorted({i: alp.count(i) for i in alp}.items(), key=value_sort):
        print(char, ":", "".join(["-" if i % 5 else "-|" for i in range(1, count+1)]).rstrip("|"))
main(input())
