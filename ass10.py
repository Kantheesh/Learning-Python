'''
10. Perform below operations on string
		# search and replace
	a. 	inp = "c:/home/test/abc.py"
		update this to : c:\home\test\abc.py
	b. 	inp = "google.com"
		remove '.com' from above string
		output : print(inp) # google
	c.	inp = "google.com"
		find the position of '.' in above string
'''

inp = "c:/home/test/abc.py"
print(inp)
inp = inp.replace("/","\ ")
print(inp)
print("-------------------------------------------")

inp = "google.com"
print(inp)
inp = inp.replace(".com", "")
print(inp)
print("-------------------------------------------")

inp = "google.com"
print(inp.find("."))
