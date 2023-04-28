'''FibonacciRecursionV1'''
def fibonacci(num):
    '''FibonacciRecursionV1'''
    if num <= 0:
        return abs(num)
    return fibonacci(num-1)+fibonacci(num-2)
def main():
    '''FibonacciRecursionV1'''
    result = int(input())
    print(fibonacci(result))
main()
