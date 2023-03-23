def collatz(n):
    print(n)
    if n == 1:
        return
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)