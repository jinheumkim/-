while True:
    n = int(input())
    if n == -1:
        break
    divisor = []
    perfect = 0
    for i in range(1,(n//2)+1):
        if n % i == 0:
            divisor.append(i)
    for j in range(len(divisor)):
        perfect += divisor[j]
    if perfect == n:
        print(n, " = " , " + ".join(str(i) for i in divisor),sep ="")
    else :
        print(n,"is NOT perfect.")