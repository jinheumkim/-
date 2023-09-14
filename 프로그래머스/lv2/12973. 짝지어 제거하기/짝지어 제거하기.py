def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        while len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                break
            else:
                break
    if stack == []:
        return 1
    return 0