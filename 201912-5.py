U = [314882150829468584,
    427197303358170108,
    1022292690726729920,
    1698479428772363217,
    2006101093849356424]

def f(x):
    return x % 2009731336725594113 % 2019

n, q = map(int,input().split())
a = [i for i in range(1,n+1)]
for i in range(q):
    l, r = map(int,input().split())
    s = 0
    for j in range(l-1,r):
        s += f(a[j])
    print(s)
    t = s % 5
    for j in range(l-1,r):
        a[j] *= U[t]