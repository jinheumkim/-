def solution(arr):
    answer = []
    arr.pop(arr.index(min(arr)))
    answer = arr
    if not answer:
        answer = [-1]
    return answer