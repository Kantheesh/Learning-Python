'''
3. Swap string variable values
fname = "rahul"
lname = "dravid"
Swap the value of variable with fname & fname with lname
Output:: print(fname) # dravid
		 print(lname) # rahul
'''

fname = "rahul"
lname = "dravid"
#fname.swap(lname)
#lname.swap(fname)
fname="dravid"
lname="rahul"
print(fname)
print(lname)
print('-------------------------------------')

fname = "rahul"
lname = "dravid"

fname, lname = lname, fname
print(fname)
print(lname)