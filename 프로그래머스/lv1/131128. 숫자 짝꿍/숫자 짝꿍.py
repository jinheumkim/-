def solution(X, Y):
    answer = []
    Xdict = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
    Ydict = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
    for i in X:
        Xdict[int(i)] += 1
    for j in Y:
        Ydict[int(j)] += 1
    for key,value in Xdict.items():
        if key in Ydict.keys():
            while Xdict[key] > 0 and Ydict[key] >0:
                answer.append(key)
                Xdict[key] = Xdict.get(key) - 1
                Ydict[key] = Ydict.get(key) - 1
    answer.sort(reverse = True)
    answer =''.join(str(s) for s in answer)
    if answer == "":
        return "-1"
    if answer.count('0') == len(answer):
        return "0"
    return answer
