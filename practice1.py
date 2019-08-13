#sum of even & odd indices, diff b/w them.....
inp=str(input())
inp=list(inp)
print(inp)
a=0
b=0
for i in range(0,len(inp)):
	if i%2 == 0:
		a += int(inp[i])
	else:
		b += int(inp[i])
if a > b:
	c = a - b
else:
	c = b - a
print(c)