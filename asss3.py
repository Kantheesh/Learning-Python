#3. Swap string variable values
#fname = "rahul"
#lname = "dravid"
#Swap the value of variable with fname & fname with lname
#Output:: print(fname) # dravid
#		 print(lname) # rahul
fname="rahul"
lname="dravid"

temp=fname
fname=lname
lname=temp
print('fname after swap:{}'.format(fname))
print('lname after swap:{}'.format(lname))
