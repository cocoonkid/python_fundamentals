'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

month_list = ["January", "February", "March", "April","May", "June", "July", "August", "September", "October", "November", "December"]

num = int(input("Please enter a number: \n"))

if num in range(13):
    print(month_list[num - 1])
else:
    print("other")


