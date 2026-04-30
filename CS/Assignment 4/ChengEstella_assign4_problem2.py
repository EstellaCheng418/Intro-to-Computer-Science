# Name: Estella Cheng
# Date: September 30, 2025
# Class Section: 001
# Assignment 04_Problem #2: 21

import random

print("Let's Play 21...")

# Get random cards (2–10, Ace = 11)
cards = [2,3,4,5,6,7,8,9,10,11]
dealer_cards = [random.choice(cards), random.choice(cards)]
player_cards = [random.choice(cards), random.choice(cards)]

# Show dealer's first card and hide the second
print("Here are the dealer's cards:", dealer_cards[0], "X")

# Show player's cards
print("Turn: Player")
print("Here are your cards:", player_cards[0], player_cards[1])

# Calculate sums
dealer_sum = sum(dealer_cards)
player_sum = sum(player_cards)

# Flag to stop dealer if game ended during player turn
game_over = False

# Player's turn (Check if the game ends or not)
while True:
    if player_sum == 21:
        print("The Player has 21!")
        print("The Player wins!")
        game_over = True
        break

    if player_sum > 21:
        print("The Player goes bust!")
        print("The Dealer wins!")
        game_over = True
        break

    # Player's next move
    Decision = input("What would you like to do? (Hit/Stay) ").lower()

    if Decision == "hit":
        # Draw a new card
        new_card = random.choice(cards)
        player_cards = player_cards + [new_card]   # add the new card
        player_sum = sum(player_cards)             # update player's sum

        # Print player's cards
        print("Here are your cards:", end=" ")
        for c in player_cards:
            print(c, end=" ")
        print()

        # Check outcomes after the draw
        if player_sum == 21:
            print("The Player has 21!")
            print("The Player wins!")
            game_over = True
            break

        if player_sum > 21:
            print("The Player goes bust!")
            print("The Dealer wins!")
            game_over = True
            break

        # otherwise continue the loop (ask hit/stay again)

    else:
        # Player decides to stay，move to dealer
        break

# Dealer's turn (only if the player hasn't won or busted)
if not game_over:
    print("Turn: Dealer")
    print("Here are your cards:", dealer_cards[0], dealer_cards[1])

    # Dealer draws only one card if sum <= 16
    dealer_sum = sum(dealer_cards)
    if dealer_sum <= 16:
        print("Your cards total to 16 or less. You must take another card.")
        new_card = random.choice(cards)
        dealer_cards = dealer_cards + [new_card]
        # show dealer's cards
        print("Here are your cards:", end=" ")
        for c in dealer_cards:
            print(c, end=" ")
        print()

    # Recalculate dealer sum after draw
    dealer_sum = sum(dealer_cards)

    # Decide outcome
    if dealer_sum == 21:
        print("The Dealer has 21!")
        print("The Dealer wins!")
    elif dealer_sum > 21:
        print("The Dealer goes bust!")
        print("The Player wins!")
    elif dealer_sum == player_sum:
        print("It's a tie!")
    else:
        print("The Player has", player_sum, "and the Dealer has", dealer_sum, ".")
        # who is closer to 21 wins
        if (21 - player_sum) < (21 - dealer_sum):
            print("The Player wins!")
        elif (21 - player_sum) > (21 - dealer_sum):
            print("The Dealer wins!")
        else:
            print("It's a tie!")
