'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

<<<<<<< HEAD
'''


y = input("Please enter 10 numbers seperated by comma: ")
y = y.replace(","," ")
y = y.split(" ")
counter = 1

for element in y:
    element = int(element)
    counter *= element
else:
    print(counter)


largestnum = y[0]
for largest in y:
    if largest > largestnum:
        largestnum = largest
else:
    print(largestnum)











=======
CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
>>>>>>> a2559241a173d7e0ba741a8d44f5da6351605420
