'''
Write a script that creates a list of all unique values in a list. For example:

<<<<<<< HEAD
_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
=======
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
>>>>>>> a2559241a173d7e0ba741a8d44f5da6351605420
unique_list = [55, 'hi', 4, 13]


'''
<<<<<<< HEAD


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




=======
>>>>>>> a2559241a173d7e0ba741a8d44f5da6351605420
