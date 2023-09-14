def solution(x):
    answer = 0
    list = [int(i) for i in str(x)]
    for i in range(len(list)):
        answer += list[i]
    return x % answer == 0