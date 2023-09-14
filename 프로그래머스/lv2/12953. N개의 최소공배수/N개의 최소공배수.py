def GCD(a,b):                        #유클리드 최대공약수
    a, b = max(a,b), min(a,b)
    while b!=0:
        a, b = b, a%b      
    return a

def LCM(a,b):                        #유클리드 최소공배수
    result = (a*b)//GCD(a,b)
    return result

def solution(arr):
    answer = 0
    answer = LCM(arr[0],arr[1])
    for i in range(2,len(arr)):
        answer = LCM(answer,arr[i])
    return answer