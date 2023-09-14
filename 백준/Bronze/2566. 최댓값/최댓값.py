x = 0
y = 0
max_num = 0
for i in range(9):
    n = list(map(int,input().split()))
    if max_num < max(n) :
        max_num = max(n)
        x = i
        y = n.index(max_num)
print(max_num)
print(x+1, y+1)