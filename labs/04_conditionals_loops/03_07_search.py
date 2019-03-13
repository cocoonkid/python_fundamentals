'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''


num = input("Please enter a number from one to one billion! ")

while item in range(0, 1000000000):
        if item == num:
            print(item)
        else:
            break