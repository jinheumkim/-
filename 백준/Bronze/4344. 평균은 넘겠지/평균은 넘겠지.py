c = int(input())                                #케이스 개수

for _ in range(c):              
    n = list(map(int,input().split()))          #학생 수
    a = sum(n[1:])/n[0]                         #평균 값 구하기 (점수/학생수)    
    count = 0           
    for i in n[1:]:
        if i>a:
            count += 1
    print('%.3f'%(count/n[0]*100)+"%")