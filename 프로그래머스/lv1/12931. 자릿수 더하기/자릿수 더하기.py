def solution(n):
    n_list = []
    answer = 0
    n_list = [int(i) for i in str(n)]
    for i in range(len(n_list)):
        answer += n_list[i]

    return answer