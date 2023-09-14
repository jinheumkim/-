n = int(input())
count = 0                       
for i in range(1,n+1):            
    a = list(map(int,str(i)))
    if i<100:
        count += 1
    elif a[0]-a[1]==a[1]-a[2]:
        count += 1
print(count)