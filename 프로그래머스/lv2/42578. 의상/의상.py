def solution(clothes):
    answer = 1
    type = []
    count = []
    for i in range(len(clothes)):
        type.append(clothes[i][1])
    type_set = set(type)
    for i in type_set:
        count.append(type.count(i))
    for i in count:
        answer *= (i + 1)
    return answer - 1