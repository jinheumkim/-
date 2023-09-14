def solution(s):
    answer = ''
    temp = [str(i) for i in str(s)]
    if len(temp) % 2 == 0:
        for i in range((len(temp)//2)-1,(len(temp)//2)+1):
            answer += temp[i]
    else:
        for i in range(len(temp)//2,len(temp)//2+1):
            answer += temp[i]
    answer = str(answer)
    return answer