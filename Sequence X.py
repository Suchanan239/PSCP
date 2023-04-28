"""Sequence X"""
def main():
    """Sequence X"""
    n_m = int(input())
    if n_m > 0 and n_m < 100:
        for i in range(0, n_m):
            for j in range(0, n_m - i - 1):
                print(end="   ")
            for j in range(1, i+2):
                print("%02d" %j, end=" ")
            for j in range(i, 0, -1):
                print("%02d" %j, end=" ")
            print()
        for i in range(n_m, 0, -1):
            for k in range(0, n_m - i + 1):
                print(end="   ")
            for k in range(1, i):
                print("%02d" %k, end=" ")
            for k in range(i - 2, 0, -1):
                print("%02d" %k, end=" ")
            print()
main()
