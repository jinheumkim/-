def solution(n):
    b_number = []
    result = 0
    while n >0 :
        b_number.append(n%3)
        n = n//3
    print(b_number)
    b_number.reverse()
    for i in range(len(b_number)):
        if b_number[i] == 1 or 2:
            result += b_number[i]*3**(i)
        else:
            result += 0
    return result