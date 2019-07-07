'''
12. Try a string operation to perform below operation
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

exam_st_date = (11, 12, 2014)
exam_st_date = str(exam_st_date)
print(exam_st_date.replace(', ', ' / '))