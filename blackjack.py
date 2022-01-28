## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

from itertools import count
import os
import random
from art import logo
from blackjack_functions import total_score
from blackjack_functions import has_blackjack
from blackjack_functions import draw
from blackjack_functions import optimize_hand

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
computer_hand = []

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    for num in range(0, 2):
        draw(user_hand)
        draw(computer_hand)

    print(f"\nYour cards: {user_hand}, current score: {total_score(user_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

    keep_playing = True

    if has_blackjack(computer_hand) == True:
        print("\nComputer has Blackjack. You lose.")
        keep_playing = False
    elif has_blackjack(user_hand) == True:
        print("\nBlackjack! You win.")
        keep_playing = False
    
    if keep_playing == True:
        hit_pass = input("\nType 'y' to get another card, type 'n' to pass: ")
    if hit_pass == 'y':
        keep_playing = True
    
    while keep_playing == True:
        draw(user_hand)
        user_hand = optimize_hand(user_hand)
        print(f"\nYour cards: {user_hand}, current score: {total_score(user_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")
        
        if total_score(user_hand) < 21:
            hit_pass = input("\nType 'y' to get another card, type 'n' to pass: ")
            if hit_pass == 'y':
                keep_playing = True
            else:
                keep_playing = False
        elif total_score(user_hand) == 21:
            keep_playing = False                   
        elif total_score(user_hand) > 21:
            
            keep_playing = False
            print("\nBust! You went over 21!\n")
            
    # User has lost or has decided to stop drawing cards at this point.

    computer_score = total_score(computer_hand)




else:
    print("\nGoodbye!")





