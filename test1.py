#4. Write a program to swap first & last element of any list provided
##output: print(inp) # [4,2,3,44,10]	






inp=[10,2,3,44,4]
temp=inp[0]
inp[0]=inp[-1]
inp[-1]=temp
print(inp)