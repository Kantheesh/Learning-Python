#given string consider only unique digits from it and print larger even number, if not possible to form print -1

import re
inp = input()
x = re.sub("\D", "", inp)
x = set(x)
x = list(x)
a = []
#x = str(x)
print(x)
print(len(x))
print("---------------------------------------")
for i in range(0, len(x)):
	y = int(x[i])
	a.append(y)

print(a)
print(sorted(a,reverse=True))
print(a)
		
	# print(y)
	# print(type(y))