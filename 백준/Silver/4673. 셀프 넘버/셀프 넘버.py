a = set(range(1,10001))
n = set()

for i in range(1,10001):
    for j in str(i):
        i = i + int(j)
    n.add(i)

self = sorted(a - n)
for i in self:
    print(i)