def solution(s):
    answer = ''
    answer = [str(i) for i in str(s)]
    answer.sort()
    answer = ''.join(reversed(answer))
    return answer