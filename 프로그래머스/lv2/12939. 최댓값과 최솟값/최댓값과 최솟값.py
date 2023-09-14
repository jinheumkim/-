def solution(s):
    answer = ''
    list = []
    s = s.split(" ")
    for i in s:
        list.append(int(i))
    answer = str(min(list)), str(max(list))
    answer =' '.join(answer)
    return answer