def solution():
    a ,b ,c = map(int,input().split())
    d = max(a,b,c)
    if d == a:
        if a >= b + c:
            a = b + c - 1
    elif d == b:
        if b >= a + c:
            b = a + c - 1
    else:
        if c >= a + b:
            c = a + b - 1
    print(a + b + c)
solution()