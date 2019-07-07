'''
4. Write a program to swap first & last element of any list provided
inp = [10,2,3,44,4]
output: print(inp) # [4,2,3,44,10]	
'''

inp = [10,2,3,44,4]
a = inp.pop()
b = inp.pop(0)
inp.insert(0,a)
inp.append(b)
print(inp)