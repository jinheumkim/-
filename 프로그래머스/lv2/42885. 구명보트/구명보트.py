from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people != []:
        for _ in range(len(people)):
            if limit/2 >= people[0]:
                if people[-1] > limit / 2:
                    if people[0] + people[-1] > limit:
                        people.pop()
                        answer += 1
                        break
                    elif people[0] + people[-1] <= limit:
                        people.popleft()
                        people.pop()
                        answer += 1
                        break
                else:
                    answer += len(people) // 2 + len(people) % 2
                    people = []
                    break
            else :
                answer += len(people)
                people = []
                break
    return answer