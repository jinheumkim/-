def solution(s, n):
    answer = ''
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for i in list(s):
        if i in uppercase:
            answer += uppercase[(uppercase.index(i) + n) % 26]
        if i in lowercase:
            answer += lowercase[(lowercase.index(i) + n) % 26]
        if i == ' ':
            answer += i
    return answer