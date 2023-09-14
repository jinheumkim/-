n = int(input())
num = map(int,input().split())
v = int(input())
a = 0
for i in num:
    if i == v:
        a += 1
print(a)