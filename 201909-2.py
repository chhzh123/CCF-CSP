n = int(input())
flag = [False] * n
sumup = 0
for i in range(n):
    a = list(map(int,input().split()))[1:]
    n_apple = a[0]
    for d in a:
        if d > 0:
            if n_apple != d:
                flag[i] = True
                n_apple = d
        else:
            n_apple += d
    sumup += n_apple
cnt = 0
e = 0
for i in range(n):
    if flag[i]:
        cnt += 1
        if (n == 1 and flag[0]) or (n >= 2 and flag[i-1] and flag[i-2]):
            e += 1
print(sumup,cnt,e)