n = int(input())
s = list(map(int,input().split()))
cnt = {}
maxCnt = 0
maxNum = 10001
for i in range(n):
	num = s[i]
	cnt[num] = cnt.get(num,0) + 1
	if cnt[num] > maxCnt or (cnt[num] == maxCnt and num < maxNum):
		maxCnt = cnt[num]
		maxNum = num
print(maxNum)