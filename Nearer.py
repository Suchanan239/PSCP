'''Nearer'''
def main():
    '''Nearer'''
    alice = int(input())
    bob = int(input())
    car = int(input())
    a_c = abs(car-alice)
    b_c = abs(car-bob)
    if a_c < b_c:
        print("Alice", a_c)
    elif b_c < a_c:
        print("Bob", b_c)
    elif a_c == b_c:
        print("Sundaes", a_c)
main()
