def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer