'''
15. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
sample:: a = (4,5)
		 b = (2,4)
output:: (2,1)
'''

a = (4,5)
b = (2,4)

x = a[0]-b[0]
y = a[1]-b[1]
z = x,y

print(tuple(z))
