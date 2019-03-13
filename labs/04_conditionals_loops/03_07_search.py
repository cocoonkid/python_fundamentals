'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''


num = int(input("Please enter a number from one to one billion!: \n "))

counter = 0

while counter < 100:
    counter += 1
    if counter == num:
        print("Your numbers is " + str(counter) + " !")






