'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

counter = 0

while counter < 1001:
    counter += 1
    if counter % 5 == 0:
        print(counter)