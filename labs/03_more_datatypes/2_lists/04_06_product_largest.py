'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.

Print the results.

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











