'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''




append = "ay"
word = input("Please tell me your word so I can transform it to pig latin: ")
word= word.lower()
result = word[1:] + word[0]
print(result + append)

