n = int(input())
cnt = [0] * 4
cntall = 0
p = 0
c = 0
while cntall <= n:
    c += 1
    if c % 7 == 0 or "7" in str(c): # skip
        cnt[p] += 1
    else:
        # print(p,c)
        cntall += 1
    p += 1
    if p == 4:
        p = 0
for i in range(4):
    print(cnt[i])