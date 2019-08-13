#fl = open(r"---path---")
# x = fl.read()
# fl.close()
# x = [1,1,1,1,2,2,2,2,3,3,3]
# for i in x:
	# if i == i+1:
		# print(i)
		# print(i+1)
	
'''
def arrOddOcc(arr, arr_len): 
      
    for i in range(0, arr_len): 
        c = 0                                      #10^10 == 00^10 == 10^10 == 00 ^11 == 11
        for j in range(0, arr_len): 
            if arr[i] == arr[j]: 
                c = c+1
              
        if (c % 2 != 0): 
            return arr[i] 
          
    return -1
a = input()
print("Enter array numbers you need to check:")

k = list(a)
b = len(k)
print(arrOddOcc(k,b))
'''

#// [1,2,7,1] --- 9 
#[1], [2], [3] [2,7] == 9 sub arrays length---- 9 


def sub_list(b):
	sublist = [[]]
	for i in range(len(b)+1):
		for j in range(i+1, len(b)+1):
			sub = b[i:j]
			sublist.append(sub)
	return sublist
a = [1,2,7,1]
x = sub_list(a)
print(x)	

