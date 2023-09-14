def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
        print(d)
    return len(d)