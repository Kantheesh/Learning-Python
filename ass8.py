'''
8. Update list as suggested below
inp = ['Ramesh', 'Bangalore', 'Vijay', 'Kiran', 'Ramesh']
	a. Remove Bangalore from the list
	b. Get count of Ramesh # 2
	c. Print highest index of list
	d. Change Vijay to Ajay
	e. Add 'Rahul' at the end
'''

inp = ['Ramesh', 'Bangalore', 'Vijay', 'Kiran', 'Ramesh']

print("------------------------------------------------------")
inp.remove('Bangalore')
print(inp)
print("------------------------------------------------------")

b = inp.count('Ramesh')
print(b)
print("------------------------------------------------------")

c = inp.index('Ramesh', 1)
print(c)
print("------------------------------------------------------")

inp[2] = 'Ajay'
print(inp)
print("------------------------------------------------------")

inp.insert(100, 'Rahul')
print(inp)