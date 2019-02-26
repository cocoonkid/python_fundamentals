'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''



text1=input("Please give me a text: ")
text2=input("Please give me a text: ")
text3=input("Please give me a text: ")
num1 = len(text1)
num2 = len(text2)
num3 = len(text3)

if (num1 > num2) and (num1 > num3):
    print(text1)
elif num2 > num1 and num2 > num3:
    print(text2)
elif num3 > num1 and num3 > num2:
    print(text3)
else:
    print("There is no longest text.")




