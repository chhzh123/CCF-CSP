n = int(input())
score = [0] * 5
lst = []
for i in range(n):
    lst.append(tuple(map(int,input().split())))
for point in lst:
    x,y = point # have rubbish
    if (x,y+1) in lst and (x,y-1) in lst and (x+1,y) in lst and (x-1,y) in lst:
        cnt = 0
        if (x+1,y+1) in lst:
            cnt += 1
        if (x+1,y-1) in lst:
            cnt += 1
        if (x-1,y+1) in lst:
            cnt += 1
        if (x-1,y-1) in lst:
            cnt += 1
        score[cnt] += 1
for i in range(5):
    print(score[i])