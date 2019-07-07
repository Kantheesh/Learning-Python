'''
pop():
	--> pop is a method that can take arguments as index
	--> it can be stored to another object
	
remove():
	-->remove is a method that can take arguments as object(which we need to remove )
	-->it can't be stored to an another object
'''

#        0      1      2      3      4
inp = ['abc', 'def', 'ghi', 'jkl', 'mno']

x = inp.pop(2)

print(x)
print(inp)
print("-----------------------------------------------------")
inp = ['abc', 'def', 'ghi', 'jkl', 'mno']

out = inp.remove('def')
print(out)
print(inp)