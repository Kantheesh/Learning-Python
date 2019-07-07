'''
16. Write a program to remove last object from a tuple
x = (11,22,33,44)
# Expected => x = (11,22,33)
'''

x = (11,22,33,44)
x = list(x)
x.pop()
x = tuple(x)
print(x)