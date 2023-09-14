def solution(n):
    answer = [0,1]
    for i in range(n):
        answer.append(answer[i] + answer[i+1])

    return answer[-2] % 1234567