def solution(s):
    cnt = 0
    zero_cnt = 0
    while True:
        if s == '1':
            return [cnt,zero_cnt]
        zero_cnt += s.count('0')
        s = bin(s.count('1'))[2:]
        cnt += 1