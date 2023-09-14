def solution(s):
    answer = 0
    stack = []
    if len(s) % 2 != 0:
        return 0
    for _ in range(len(s)):
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2:
                if (stack[-1] == ")" and stack[-2] == "(") or (stack[-1] == "}" and stack[-2] == "{" )or (stack[-1] == "]" and stack[-2] == "["):
                    stack.pop()
                    stack.pop()
                if (i == len(s) -1) and stack == []:
                    answer += 1
                    break
                elif (i == len(s) -1) and stack != []:
                    stack = []
                    break
        s = s[1:] + s[:1]
    return answer