a = int(input())
e = a
count = 0
while True:
    b = e//10
    c = e%10
    d = (b+c)%10
    e = (c*10)+d
    count += 1
    if a == e:
        break
print(count)