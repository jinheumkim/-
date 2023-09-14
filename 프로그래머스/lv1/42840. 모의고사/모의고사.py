def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    onecnt = 0
    twocnt = 0
    threecnt = 0

    for i in range(0,len(answers)):
        if one[i%5] == answers[i]:
            onecnt += 1
        if two[i%8] == answers[i]:
            twocnt += 1
        if three[i%10] == answers[i]:
            threecnt += 1
    
    rank = max(onecnt,twocnt,threecnt)

    if rank == onecnt:
        answer.append(1)
    if rank == twocnt:
        answer.append(2)
    if rank == threecnt:
        answer.append(3)

    return answer