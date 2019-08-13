#to check given string is keyword or not....
import keyword
k = keyword.kwlist
print("keywords in list are:",k)
inp = str(input("enter some string:"))
if inp in k:
	print("given string '"+inp+"' is keyword")
else:
	print("given string '"+inp+"' is not keyword")