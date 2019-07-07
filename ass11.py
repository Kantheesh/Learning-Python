'''
11. Creating below mapping data in dictionary
	name - ajay
	rn   - 10
	pan  - chxp34545s1
	
	Get a keyboard input & display data which is mapped to input
	ex: if keyboard input is name then display ajay
'''

data = {}

data['name'] = 'ajay'
data['rn'] = 10
data['pan'] = 'chxp34545s1' 
print("enter the key you need to display:")
out = input()
#if out == 'name' || 'rn' || 'pan' :
print(data[out])
#else
#print("enter valid input...")