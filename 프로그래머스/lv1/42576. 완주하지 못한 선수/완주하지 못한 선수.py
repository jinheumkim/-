def solution(participant,completion):
    answer = []
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        completion.append(0)
        if participant[i] != completion[i]:
            answer.append(participant[i])
            break
    return answer[0]