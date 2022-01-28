import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def has_ace(hand):
    """Checks if a given hand has an Ace."""
    if 11 in hand:
        return True
    else:
        return False

def total_score(hand):
    """Calculates the total of a hand and returns the score."""
    return sum(hand)

def has_blackjack(hand):
    """Determines if a hand is a Blackjack."""
    if len(hand) == 2 and total_score(hand) == 21:
        return True
    else:
        return False

def draw(hand):
    """Draws from a list of cards."""
    hand.append(random.choice(cards))

def winner(user_score, computer_score):
    if user_score < computer_score and computer_score <= 21:
        return "You lose."
    elif user_score > 21:
        return "You lose."
    elif user_score == computer_score:
        return "Draw."
    elif user_score > computer_score and user_score <= 21:
        return "You win."
    elif computer_score > 21:
        return "You win."

def optimize_hand(hand):
    cont_optimization = has_ace(hand)
    while cont_optimization == True:
        if total_score(hand) > 21:
            hand[hand.index(11)] = 1
        else:
            cont_optimization = False
    
    return hand