'''
Code a game of rock paper scissors.

'''
from random import randint

#0 = scissor, 1 = rock, 2 = paper
# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    if hand == 0:
        return "scissor"
    elif hand == 1:
            return "rock"
    elif hand == 2:
            return "paper"
        # for example if the variable hand is 0, it should return the string "scissor"
    else:
            pass

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
   if random == hand:
       print("You tied!")
   elif random > hand and random != "paper":
       print("You lost!")
   elif  random < hand and random != "scissor":
       print ("You won")




'''
Start here
'''

# take in a number 0-2 from the user that represents their hand

hand = int(input("Please enter a number: 0 = scissor, 1 = rock, 2 = paper \n"))


# generate a random number 0-2 to use for the computer's hand

random = (randint(0, 3))

# call the function get_hand to get the string representation of the user's hand

player = get_hand(hand)


# call the function get_hand to get the string representation of the computer's hand

computer = get_hand(random)

# call the function determine_winner to figure out the winner


determine_winner(computer,player)

# print out the player hand and computer hand

print("Its a human " + str(player) + " versus a computer " + str(computer) + "!")

# print out the winner


print("The winner is "  )
