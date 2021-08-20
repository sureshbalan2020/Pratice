def fibonacci_series(n):

    if n == 0 or n == 1:
        return n
    else:
        minus2 = 0
        minus1 = 1
        for i in range(n-1):
            result = minus2 + minus1
            minus2 = minus1
            minus1 = result
        return result
for i in range(36):
    print(fibonacci_series(i))

