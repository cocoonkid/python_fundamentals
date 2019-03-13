'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''


text = input("Please give me a string! \n")
text = list(list(text))
print(text)


index = 0
temp_list = []
list_of_chars = []

for element in text:
    temp_list.append(element)
    list_of_chars = list(temp_list)
    index += 1

print(list_of_chars)
list_of_chars = (list_of_chars)


#tuple_of_chars = tuple(list_of_chars.split(" "))



print(list_of_chars)

#print(tuple_of_chars)

