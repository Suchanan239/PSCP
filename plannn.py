"""plannn"""
def main():
    """plannn"""
    w_d = input()
    n_1 = float(input())
    n_2 = float(input())
    n_3 = float(input())
    if n_1 > n_2:
        n_1, n_2 = n_2, n_1
    if n_2 > n_3:
        n_2, n_3 = n_3, n_2
    if n_1 > n_2:
        n_1, n_2 = n_2, n_1
    if w_d == "Ascend":
        print("%.2f, %.2f, %.2f" %(n_1, n_2, n_3))
    if w_d == "Descend":
        print("%.2f, %.2f, %.2f" %(n_3, n_2, n_1))
main()
