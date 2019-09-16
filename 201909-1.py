n,m = list(map(int,input().split()))
original = 0
maxD = 0
index = 1
for i in range(n):
    a = list(map(int,input().split()))
    original += a[0]
    delete = sum(a[1:])
    original += delete
    if maxD < -delete:
        maxD = -delete
        index = i+1
print(original,index,maxD)