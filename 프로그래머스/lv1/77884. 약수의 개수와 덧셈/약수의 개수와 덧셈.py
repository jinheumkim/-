def solution(left, right):
    result = 0
    for i in range(left, right+1):
        divisor = []
        for j in range(1,i+1):
            if i % j== 0:
                divisor.append(j)
        if len(divisor) % 2 ==0:
            result += i
            divisor = []
        elif len(divisor) % 2 -1 == 0:
            result -= i
            divisor = []
                
    return result