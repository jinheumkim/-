def solution(phone_number):
    answer = ''
    p_num = [int(i) for i in str(phone_number)]
    for i in range(len(p_num)-4):
        p_num[i:-4] = ['*']
    for i in range(len(p_num)):
        answer += str(p_num[i])
    return answer
