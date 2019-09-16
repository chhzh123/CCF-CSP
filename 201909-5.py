n, m, k = list(map(int,input().split()))
important = list(map(int,input().split()))
important.sort()
tree = [0] * n

def add_edge(a,b,c):
    if tree[a-1] == 0:
        tree[a-1] = [(b-1,c)]
    else:
        tree[a-1].append((b-1,c))

for i in range(n-1):
    a, b, c = list(map(int,input().split()))
    add_edge(a,b,c)
    add_edge(b,a,c)

dis = []
for i in range(n):
    dis.append([0]*n)

def DFS(prev,node,cost):
    dis[src][node] = cost
    dis[node][src] = cost
    for next in tree[node]:
        if next[0] == prev:
            continue
        else:
            DFS(node,next[0],cost+next[1])

for i in range(n//2+1):
    src = i
    DFS(-1,i,0)
weights = []
for i in important:
    for j in important:
        if i < j:
            weights.append((dis[i-1][j-1],i,j))
weights.sort()
# print(weights)
node_lst = [weights[0][1],weights[0][2]]
sumup = weights[0][0]
cnt = 2
for edge in weights[1:]:
    if cnt >= k:
        break
    else:
        if edge[1] in node_lst:
            cnt += 1
            sumup += weights[i][0]
            node_lst.append(edge[2])
        elif edge[2] in node_lst:
            cnt += 1
            sumup += weights[i][0]
            node_lst.append(edge[1])
print(sumup)