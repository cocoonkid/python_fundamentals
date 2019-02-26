'''
Write a script that creates a list of all unique values in a list. For example:

_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''


list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
seen = []
unique_list=[]

for element in list:
    x  = list.count(element)
    if x > 1:
        seen.append(element)
    else:
        unique_list.append(element)

print(unique_list)




