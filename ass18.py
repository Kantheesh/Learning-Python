'''
18. Write a program to convert values of a dictionary to tuple
data = {11:22,33:44,55:66}
# Expected out = (22,44,66)
'''

data = {11:22,33:44,55:66}
k = data.values()
print(k)
out = tuple(k)
print(out)