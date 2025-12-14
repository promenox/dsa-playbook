# practice recursion by calculating fibonacci numbers

# pattern: [0, 1,] <- base
# | 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., n
# | 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, ..., i
# n_th is found by adding n-1 and n-2

def fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
