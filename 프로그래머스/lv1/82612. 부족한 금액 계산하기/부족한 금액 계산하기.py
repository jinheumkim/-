def solution(price, money, count):
    answer = 0
    temp = 0
    for i in range(1,count+1):
        temp += price * i
        if money < temp :
            answer = temp - money
    else :
        return answer