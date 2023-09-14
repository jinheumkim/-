def solution(N, stages):
    answer = []
    fail = []
    fail_percent = []
    dic = {}
    for i in range(1,N+1):
        fail.append(stages.count(i))
    s = len(stages)
    print(fail)
    for i in range(N):
        if i == 0:
            fail_percent.append(fail[i]/s)
        elif fail[i] == 0:
            fail_percent.append(fail[i]/s)
            if s-fail[i-1] != 0:
                s -= fail[i-1]
        else :
            s -= fail[i-1]
            if s == 0:
                fail_percent.append(1)
            else:
                fail_percent.append(fail[i]/(s))
    print(fail_percent)
    for i in range(len(fail_percent)):
        dic[i] = fail_percent[i]
    sdic = dict(sorted(dic.items(), key = lambda x : x[1] ,reverse = True))
    answer = (list(sdic.keys()))
    for i in range(len(answer)):
        answer[i] += +1

    return answer