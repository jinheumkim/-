A, B = input().split()
C = int(input())

X = (int(A)+(int(B)+int(C))//60)%24
Y = (int(B)+int(C))%60
print(X,Y)