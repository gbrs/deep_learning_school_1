def almost_double_factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n + 1, 2):
        prod *= i
    return prod


print(almost_double_factorial(3))
