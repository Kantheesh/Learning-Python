# isdecimal -> given a string, check if it is decimal
# return/result of the method is True/False
# if valid decimal -> True
# if not valid decimal -> False

inp1 = "1099191992929943949"
out = inp1.isdecimal()
print(out) # True

inp1 = "10a"
out = inp1.isdecimal()
print(out)

inp1 = "10.67"
out = inp1.isdecimal()
print(out)

inp1 = "1 2"