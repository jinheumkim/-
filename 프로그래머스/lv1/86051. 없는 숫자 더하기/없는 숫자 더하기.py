def solution(numbers):
    answer = 0
    number = [0,1,2,3,4,5,6,7,8,9]
    number =[x for x in number if x not in numbers]
    for i in range(len(number)):
        answer += number[i]
        
    return answer


