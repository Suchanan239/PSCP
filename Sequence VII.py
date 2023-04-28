"""Sequence VII"""
def main():
    """Sequence VII"""
    n_m = int(input())
    for i in range(1, n_m+1):
        for k in range(1, i+1):
            print(k, end=" ")
        print("\r")
    for i in range(n_m-1, 0, -1):
        for k in range(1, i+1):
            print(k, end=" ")
        print("\r")
main()
