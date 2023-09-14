def solution(nums):
    answer = 0
    number = nums
    number = set(number)
    number = list(set(number))
    num = []
    for i in range(len(nums)//2):
        if len(nums)//2 > len(number):
            num = number
        else :
            num.append(number[i])

    for i in range(len(num)):
        answer += 1
    
    return answer