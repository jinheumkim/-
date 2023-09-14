def bin(number):
    result = "" 
    while number:
        b_number = number%2
        number = number//2
        result = str(b_number) + result
    return result
def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in range(len(arr1)):
        map1.append(''.join(bin(arr1[i])))
        if len(map1[i]) < n:
            map1[i] = '0'*(n- len(map1[i])) + map1[i]
    for j in range(len(arr2)):
        map2.append(''.join(bin(arr2[j])))
        if len(map2[j]) < n:
            map2[j] = '0'*(n- len(map2[j])) + map2[j]
    for x in range(n):
        temp = []
        for y in range(n):
            if map1[x][y] == '0' and map2[x][y] == '0':
                temp.append(' ')
            else:
                temp.append('#')
        answer.append(temp)
    answer2 = []
    for array in answer:
        answer2.append(''.join(array))

    return answer2