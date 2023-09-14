def solution(n,m):
    r = m
    s = n
    n, m = max(n,m), min(n,m)
    while m != 0:
        n, m = m, n%m

    return [n,(s*r)//n]