def solution(n,a,b):
    answer = 0
    if a < b:
        for i in range(0,n//2 + n%2):
            if a == b - 1 and a % 2 == 1 and b % 2 == 0:
                break
            a = a // 2 + a % 2
            b = b // 2 + b % 2
            answer += 1
    elif a > b:
        for i in range(0,n//2 + n%2):
            if b == a - 1 and b % 2 == 1 and a % 2 == 0:
                break
            a = a // 2 + a % 2
            b = b // 2 + b % 2
            answer += 1
    return answer +1
