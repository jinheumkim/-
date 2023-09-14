def solution(brown, yellow):
    answer = []
    list  = []
    carpet = brown + yellow
    for i in range(3,(carpet//3) + 1):
        j = carpet / i
        if (j * 10) % 10 != 0:
            continue
        list.append(int(j))
    print(list)
    for i in range(len(list)):
        if yellow == (list[i]-2) * (list[-i-1]-2):
            answer.append(list[i])
            answer.append(list[-i-1])
            break
    return answer
