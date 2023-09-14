def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] >= 2:
            answer += str(i) * (food[i] // 2)
    reverse = answer[::-1]
    answer += str(0)
    answer += reverse
    return answer