from queue import PriorityQueue

m,n = list(map(int,input().split()))
a = []
for i in range(m):
    a.append([0] * n)
for j in range(n):
    cid, score = list(map(int,input().split()))
    for i in range(m):
        a[i][j] = ((i,cid,score))
for i in range(m):
    a[i].sort(key=lambda x: x[2],reverse=True)
op = int(input())
for step in range(op):
    # print(a)
    lst = list(map(int,input().split()))
    if int(lst[0]) == 1: #add
        ty, commodity, score = int(lst[1]), int(lst[2]), int(lst[3])
        for i in range(len(a[ty])+1): # can be replaced by binary search
            if i == len(a[ty]) or score > a[ty][i][2]:
                a[ty].insert(i,(ty,commodity,score))
                break
    elif int(lst[0]) == 2: #delete
        ty, commodity = int(lst[1]), int(lst[2])
        for i in range(len(a[ty])):
            if a[ty][i][1] == commodity:
                del a[ty][i]
                break
    else: # int(lst[0]) == 3 #select
        K = lst[1]
        sel = lst[2:]
        res = []
        for (i,index) in enumerate(sel):
            res += a[i][:index]
        # print(res)
        res.sort(key=lambda x: (x[2],-x[0],-x[1]),reverse=True)
        res = res[:K]
        res_lst = [0]*m
        for commodity in res:
            if res_lst[commodity[0]] == 0:
                res_lst[commodity[0]] = [commodity[1]]
            else:
                res_lst[commodity[0]].append(commodity[1])
        for i in range(m):
            if res_lst[i] == 0:
                print(-1)
            else:
                res_lst[i].sort()
                print(*(res_lst[i]))