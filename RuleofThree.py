"""RuleofThree"""
def main():
    """main"""
    num = int(input())
    result = 0
    final_ans = (0, 0)
    for _ in range(num):
        price = float(input())
        weight = float(input())
        if weight/price > result:
            result = weight/price
            final_ans = (price, weight)
        elif weight/price == result and price < final_ans[0]:
            result = weight/price
            final_ans = (price, weight)
    print("%.2f %.2f"%final_ans)
main()
