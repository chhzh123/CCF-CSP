import copy

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append([])
for i in range(m):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)

blocks = []
# time 0, 1
curr_t = 1
for t in range(curr_t):
    blocks.append([])
    for i in range(n):
        blocks[t].append([0])

delay, k = map(int,input().split()) # delay, # of operations
ops = []
max_t = 0
for i in range(k):
    op = list(map(int,input().split()))
    if len(op) == 3:
        node, ti, blk_num = op
        ops.append((ti,1,node,blk_num)) # created
        max_t = max(max_t,ti)
    else: # query
        node_a, q_time = op
        ops.append((q_time,2,node_a))
        max_t = max(max_t,q_time)
ops.sort()

t = 0
while len(op) != 0:
    # print(t)
    op = ops.pop(0)
    while op[0] <= t:
        blocks.append(copy.deepcopy(blocks[-1]))
        t += 1
    if t > max_t:
        break
    if op[1] == 0: # update
        _, _, node, from_node = op
        message = blocks[t-delay][from_node].copy()
        if len(message) > len(blocks[t][node]) or (len(message) == len(blocks[t][node]) and message[-1] < blocks[t][node][-1]):
            blocks[t][node] = message
            for neigh in graph[node]:
                if t + delay <= max_t:
                    ops.append((t+delay,0,neigh,node)) # send messages
    elif op[1] == 1: # create
        _, _, node, blk_num = op
        # print(blocks)
        blocks[t][node].append(blk_num)
        for neigh in graph[node]:
            if t + delay <= max_t:
                ops.append((t+delay,0,neigh,node)) # placeholder
    else: # query
        _,_,node = op
        print(*blocks[t][node])
    ops.sort()