'''
21. Write a program to insert a key 10 value 20 into below dictionary
x = {11:22,33:44}
# Expected output: x = {11:22,33:44,10:20}
'''

x = {11:22,33:44}
y = {10:20}
x.update(y)
print(x)