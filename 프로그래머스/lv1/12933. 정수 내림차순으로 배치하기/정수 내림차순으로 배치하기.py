def solution(n):
    answer = 0
    n_list = [int(i) for i in str(n)]
    n_list.sort()
    for i in range(len(n_list)):
        answer += n_list[i]*10**i
 
    return answer