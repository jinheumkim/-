n = int(input())
for _ in range(n):
    score = 0
    count = 0
    a = input()
    for i in range(len(a)):
        if a[i] == "O":
            count = count +1
            score = score + count
        elif a[i] == "X":
            count = 0
    print(score)