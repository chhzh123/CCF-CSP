# 0<-1 2<-3
n = int(input())
res = 0
# 2 (0,2) 1 (1,2) 3 (1,3)
# - 2 (2) 1 (1,2) 3 (1,3)
# 2 (0,2) 3 (0,3) 1 (1,3)
# - 2 (2) 3 (3)   1 (1,3)

# for first_one in range(2,n):
# 	for first_three in range(first_one+1,n+1):
# 		cnt = 2**(n-3) - 2**(n-first_one-1)
# 		res = (res + cnt) % 1000000007
# 		print(first_one,first_three,cnt)
# for first_three in range(2,n):
# 	for first_one in range(first_three+1,n+1):
# 		cnt = 2**(n-3) - 2**(n-first_one)
# 		res = (res + cnt) % 1000000007
# 		print(first_one,first_three,cnt)

# for first_one in range(2,n):
# 	cnt = (2**(n-3) - 2**(n-first_one-1)) * (n-first_one)
# 	res = (res + cnt) % 1000000007
# 	print(first_one,cnt)
# for first_one in range(3,n+1):
# 	cnt = (2**(n-3) - 2**(n-first_one)) * (first_one-2)
# 	res = (res + cnt) % 1000000007
# 	print(first_one,cnt)

for first_one in range(2,n+1):
	if first_one == 2:
		cnt = (2**(n-3) % 1000000007 - 2**(n-first_one-1) % 1000000007) * (n-first_one) % 1000000007
	elif first_one == n:
		cnt = (2**(n-3) % 1000000007 - 2**(n-first_one) % 1000000007) * (first_one-2) % 1000000007
	else:
		cnt = (2**(n-3) % 1000000007)*(n-2) % 1000000007 \
			- (2**(n-first_one-1) % 1000000007)*(n-first_one) % 1000000007 \
			- (2**(n-first_one) % 1000000007)*(first_one-2) % 1000000007
	res = (res + cnt) % 1000000007
	# print(first_one,cnt)
print(res % 1000000007)