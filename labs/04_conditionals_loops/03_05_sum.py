'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''


a = int(input("Please enter the lower bound: "))
b = int(input("Please enter the upper bound: "))

sum_of_numbers = 0

for item in range(a, b +1):
    sum_of_numbers += item



print(sum_of_numbers)


