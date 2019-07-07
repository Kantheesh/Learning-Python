'''
17. Find symmetric difference of 2 sets without using symmetric_difference method
x = {1,2,3,4}
y = {4,5,6,7}
# Expected out = {1,2,3,5,6,7} 
'''

x = {1,2,3,4}
y = {4,5,6,7}
a = x.difference(y)
b = y.difference(x)
out = a.union(b)
print(out)