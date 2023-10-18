def fib(n):
    if n == 0:
        return 0
    v1 = 0
    v2 = 1
    for i in range(n-1):
        v = v2
        v2 = v1 + v2
        v1 = v

    return v2
