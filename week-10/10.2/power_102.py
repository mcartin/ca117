def power(n1, n2):
    if n2 == 0:
        return 1
    else:
        return n1 * power(n1, n2-1)