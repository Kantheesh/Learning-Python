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

inp1="kantheesh karanam"
inp2="karanam"
print(inp1.capitalize(), inp2.capitalize())