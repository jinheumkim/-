a = int(input())
b = int(input())
c = int(input())
n = a*b*c
d = list(str(n))
for i in range(10):
    print(d.count(str(i)))