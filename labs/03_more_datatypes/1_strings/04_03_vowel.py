'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

text = input("Please enter a text: ")

list = ["a","e","i","o","u"]

for element in list:
        p = text.count(element)
        if p > 0:
                print(f"There is/are {p} {element}.")
        else:
                print(f"There is no {element}  in that text.")




