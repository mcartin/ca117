def sumup(n):
    if n == 0:
        return 0
    else:
        return n + sumup(n-1)