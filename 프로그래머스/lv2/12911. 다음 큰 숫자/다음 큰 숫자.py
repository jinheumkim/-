def solution(n):
    answer = 0
    cnt = 0
    cnt += bin(n)[2:].count('1')
    for i in range(n+1,n*n):
        if bin(i)[2:].count('1') == cnt :
            answer = i
            break
    return answer