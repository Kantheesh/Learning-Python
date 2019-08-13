inp = int(input())
if inp < 9:
	for i in range(0,inp+1):
		print(i,end=' ')
else:
	for j in range(0,inp+1):
		if j < 10:
			print('00',end='')
			print(j,end=' ')
		elif j >= 10:
			print('0',end='')
			print(j,end=' ')