def solution(n):
    answer = 0
    for i in range(n+1):
        if i * i == n:
            answer += i + 1
            return answer * answer
    else:
        answer = -1

    return answer