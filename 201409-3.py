target = input()
sensitive = int(input())
n = int(input())
for i in range(n):
	s = input()
	if (sensitive == 1 and s.find(target) != -1) or (sensitive == 0 and s.lower().find(target.lower()) != -1):
		print(s)