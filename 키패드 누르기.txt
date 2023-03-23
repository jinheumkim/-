def solution(numbers, hand):
    answer = ''
    dic = {1 : [0,0], 2 : [0,1], 3 : [0,2],
           4 : [1,0], 5 : [1,1], 6 : [1,2],
           7 : [2,0], 8 : [2,1], 9 : [2,2],
           '*' : [3,0], 0 : [3,1], '#' : [3,2]
           }
    
    left_s = dic['*']
    right_s = dic['#']

    for i in numbers:
        now = dic[i]
        if i in [1,4,7]:
            answer += 'L'
            left_s = now
            

        elif i in [3,6,9]:
            answer += 'R'
            right_s = now
           
        
        else:
            left_d = abs(left_s[0] - dic[i][0]) + abs(left_s[1] - dic[i][1])
            right_d = abs(right_s[0] - dic[i][0]) + abs(right_s[1] - dic[i][1])
            
            if left_d > right_d:
                answer += 'R'
                right_s = now
            
            elif left_d < right_d:
                answer += 'L'
                left_s = now
            
            else:
                if hand == 'right':
                    answer += 'R'
                    right_s = now
                else:
                    answer += 'L'
                    left_s = now
        
    return answer
