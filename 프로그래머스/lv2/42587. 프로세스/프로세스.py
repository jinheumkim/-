def solution(priorities, location):
    answer = 0
    s_p = sorted(priorities, reverse =True)
    while priorities != []:
        if location == 0:
            if priorities[0] != s_p[0]:
                priorities.append(priorities[0])
                priorities.pop(0)
                location += len(priorities)-1
            else :
                priorities.pop(0)
                s_p.pop(0)
                answer += 1
                return answer
        else :
            if priorities[0] != s_p[0]:
                priorities.append(priorities[0])
                priorities.pop(0)
                location -= 1
            else :
                priorities.pop(0)
                s_p.pop(0)
                answer += 1
                location -= 1
    return answer