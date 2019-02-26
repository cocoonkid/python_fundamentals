'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

wordcountdict = {}
text = input("Please provide me with a few words seperated by a space: ")

list = text.split()
for word in list:
    wordcount = list.count(word)
    wordcountdict[word] = wordcount

a = max(wordcountdict)
print(a)
print(wordcountdict)
