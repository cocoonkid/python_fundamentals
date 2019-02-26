'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

list1=[]
list2=[]
y = input("Please enter 10 numbers seperated by comma: ")
y = y.replace(","," ")
y = y.split(" ")

for i in range(1,11,2):
    list1.append(y[i])

for i in range(-2,-12,-2):
        list2.append(y[i])
finallist = list1+list2

for element in finallist:
    print(element, end=' ')
