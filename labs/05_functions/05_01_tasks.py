'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results



def divisible_by_4_and_7(num):
    if num % 4 == 0 and num % 7 == 0:
        print("This Number is divisible by 4 and 7! ")

def divisible_by_4_or_7(num):
    if num % 4 == 0 or num % 7 == 0:
        print("This Number is divisible by either 4 or 7! ")

def divisible_by_4_or_7_ex(num):
    if num % 4 == 0:
        print("This Number is divisible by 4  only! ")

    elif num % 7 == 0:
        print("This Number is divisible by 7  only! ")

    else:
        print("This number is not divisible by any of 4 or 7!")


num = int(input("Please enter a number from one to one billion! "))


divisible_by_4_and_7(num)

divisible_by_4_or_7(num)

divisible_by_4_or_7_ex(num)
