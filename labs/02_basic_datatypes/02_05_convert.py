'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''


x = float(10)
y = int(100.3)




a = 5
b = 2
print (a / b)
>>> 2.5
print (a // b)
>>> 2



x=input("Please enter multiplicator 1")
x=float(x)
y= input("Please enter multiplicator 2")
y=float(y)
print(x*y)


When converting floats to integers the value after the dot get lost.