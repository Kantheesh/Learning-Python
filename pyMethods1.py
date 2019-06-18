#replace()
inp="this is a test string"
print(inp.replace("is","012"))
print("----------------------------------")

inp1="80023000"
print(inp1.replace(inp1[-1],inp1[0],2))
#                      0       8     first two 0's as 8
print("----------------------------------")

#split()
inp2="kanthi is a good boy"
inp2=inp2.split()
print(inp2)
print(inp2[0])
print(inp2[1])
print(inp2[2])
print(inp2[3])
print(inp2[-1])
print("---------------------------------")
inp3="a1b1c1d1e1"
inp4="kanthi"
print(inp3.split("1"))
print(inp4.split("m"))