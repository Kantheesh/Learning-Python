inp="KANTHeesh KAranam20"
print(inp.upper())
print("-----------------------------")
print(inp[4:15].upper())
print("-----------------------------")
print(inp.lower())
print("-----------------------------")
print(inp[0:5].lower())
print("-----------------------------")
print(inp[0::2].upper(), inp[-2::-2].lower())
print("-----------------------------")
print(inp[0::2].upper(), inp[::-2].lower())
print("-----------------------------")

#capitalize()
inp1="kantheesh karanam"
inp2="karanam"
print(inp1.capitalize(), inp2.capitalize())
print("-----------------------------")

#strip(), lstrip(), rstrip()
inp3="\t \t \n ab\t  c    \t \n   "
print("input"+inp3)
print("output:"+inp3.strip()+":")
print("-----------------------------")
print("input"+inp3)
print("output:"+inp3.lstrip()+":")
print("-----------------------------")
print("input"+inp3)
print("output:"+inp3.rstrip()+":")
print("-----------------------------")

#replace()
inp4="this is a test string"
print(inp4.replace("is","012"))
