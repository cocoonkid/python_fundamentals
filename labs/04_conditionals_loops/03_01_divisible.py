'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

num = input("Please enter a number between 1 and 1,000,000,000: \n")

num = int(num)

while num > 1 and num < 1000000000:
    if num % 3 == 0:
       print("The number" + str(num) + "is divisble by 3.")
       break
    else:
        print("This number is not divisble by 3!")
        break
else:
    print ("This number is not allowed!")


