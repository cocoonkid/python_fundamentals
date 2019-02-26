'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
flattened_list=[]
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for list in starting_list:
    for element in list:
        flattened_list.append(element)


print(flattened_list)
