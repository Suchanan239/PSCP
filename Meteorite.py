'''Meteorite'''
def main():
    '''Meteorite'''
    weight = float(input())
    many = int(input())
    condition = float(input())
    increase = 0
    total = 0
    if weight < condition:
        total = 0
    else:
        while not weight < condition:
            weight = weight / many
            total += many**increase
            increase += 1
    print(total)
main()
