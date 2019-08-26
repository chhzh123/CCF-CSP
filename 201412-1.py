n = int(input())
a = list(map(int,input().split()))
cnt = [0] * 1004
for i in range(len(a)):
	cnt[a[i]] += 1
	print(cnt[a[i]],end=(" " if i != len(a)-1 else "\n"))