'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input:
Result: 4

'''


text = input("Please enter a word")
letter = input("Please enter a letter")
result= text.find(letter)

print(result)