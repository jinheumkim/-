def solution(cacheSize, cities):
    answer = 0
    LRU = []
    if cacheSize == 0:
        answer += len(cities) * 5
        return answer
    if cacheSize > len(cities):
        for i in range(len(cities)):
            LRU.append(cities[i].lower())
    else :
        for i in range(cacheSize):
            LRU.append(cities[i].lower())
    if LRU == set(LRU):
        answer += len(set(LRU)) * 5
    else :
        answer += len(set(LRU)) * 5 + (len(LRU) - len(set(LRU)))
    for i in range(cacheSize,len(cities)):
        LRU.append(cities[i].lower())
        for i in range(len(LRU)-1):
            if LRU[i] != LRU[-1]:
                if i == len(LRU)-2:
                    LRU.pop(0)
                    answer += 5
                    break
            if LRU[i] == LRU[-1]:
                answer += 1
                LRU.pop(i)
                break
    return answer