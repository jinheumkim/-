def solution(progresses, speeds):
    answer = []
    number = 0
    while progresses != []:
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            number += 1
        elif number >= 1:
            answer.append(number)
            number = 0 
        else:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
    answer.append(number)
    return answer