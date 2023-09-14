def solution(dartResult):
    answer = 0
    result = list(dartResult)
    box = []
    for i in range(len(result)):
        if result[i] == '*':
            if i == len(result)-1:
                box.append(box[-1])
                answer = sum(box)
                if result[-4] == '*':
                    box.append(2*box[-3])
                    answer = sum(box)
                elif result[-5] == '*':
                    box.append(2*box[-3])
                    answer = sum(box)
                elif result[-3] == '#':
                    box.append(box[-3]-(box[-3]//2))
                    answer = sum(box)
                elif result[-4] == '#':
                    box.append(box[-3]-(box[-3]//2))
                    answer = sum(box)
                else:
                    box.append(box[-3])
                    answer = sum(box)
            else:
                box = 2 * box
                answer = sum(box)
        if result[i] == 'S':
            if str(result[i-2]) == '1':
                box.append(10)
                answer = sum(box)
            else :
                box.append(int(result[i-1]))
                answer = sum(box)
        elif result[i] == 'D':
            if str(result[i-2]) == '1':
                box.append(100)
                answer = sum(box)
            else:
                box.append(int(result[i-1])**2)
                answer = sum(box)
        elif result[i] == 'T':
            if str(result[i-2]) == '1':
                box.append(1000)
                answer = sum(box)
            else:
                box.append(int(result[i-1])**3)
                answer = sum(box)
        elif result[i] == '#':
            box.append(-box[-1]*2)
            answer = sum(box)
    return answer