############### Blackjack Project #####################

## The deck is unlimited in size. 
## Cards are not removed from the deck as they are drawn.
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1. -> ! leave this problem for later !
## deck of cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## The computer is the dealer.
## You win when your combined value of the cards is greater than that of dealer, up to 21

## Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

#1 Create a function that uses the List deck of cards to *return* a random card. 11 is the Ace.
#2 Deal the user and computer 2 cards each. def deal_card()
#3 Create a function that takes a List of cards as input and returns the score.  def calculate_score() - use sum() maybe?
#4 Inside the function check for a blackjack (a hand with only 2 cards: ace + 10) and return 0.
# 0 will represent a blackjack in the game. - use append() and check for the one to remove
#5 Inside function check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#6 Call the function. If the computer or the user has a blackjack (0) or if the user's score is over 21, the game ends.
#7 If the game has not ended, ask the user if they want to draw another card. - a loop for the game to continue?
# If yes, then use the previous function to add another card to the user_cards List. If no, then the game has ended.
#8 The score will need to be rechecked with every new card drawn. The checks previously needs to be repeated until the game ends.
#9 Once the user is done, it's the computer turn. The computer should keep drawing cards as long as it has a score less than 17.
#10 Create a function to compare both scores. def compare(user score and computer score) 
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), 
# then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, 
# then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
#11 Ask the user if they want to restart the game. If they answer yes, start a new game. Put everything in a loop until 
# the user doesn't want to play anymore. def play_game()

import random 

def deal_card():
  """ Returns a random card from the deck """  #documentation needed as this function has an output of a random card
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):  #it's taking cards as an input 
  """ Take a list of cards and return the score calculated from the cards """
  return sum(cards)  #list of cards is iterable 
  if sum(cards) == 21 and len(cards) == 2:  #check if there's 2 cards and each is ace with 10
    return 0 
  #rule: if the score is already 21, remove the 11 from the cards and replace it with 1
  if 11 in cards and sum(cards) > 21:
    cards.remove(11) #search for first instance of element and removes it 
    cards.append(1) #adds single element to the end of the list 
  return sum(cards)

def compare(user_score, computer_score):  #function will compare both scores 
  if computer_score == user_score:
    return " This is a Draw "
  elif computer_score == 0:
    return " You lose. Computer wins "
  elif user_score == 0:
    return " You win :) "
  elif user_score > 21:
    return " You lose. Computer wins "
  elif computer_score > 21:
    return " You win :) "
  elif user_score > computer_score:
    return " You win :) "
  else:
    return " You lose. Computer wins "

def play_game():
  user_cards = []
  computer_cards = []
  game_over = False 

  for _ in range(2): #run the for loop only twice as there is only 2 cards needed
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  #When you only want to add a single item, not a list, to an existing list - then you have to use append()

  #While loop needs to be active until the game is over
  while not game_over:
    #4
    #only after dealing the cards, can we call the function to calculate the scores
    #calculate_score(user_cards)
    user_score = calculate_score(user_cards) # returns either 0 if BJ or the value of the sum of the cards
    computer_score = calculate_score(computer_cards)
    print(f"cards: {user_cards}, current score: {user_score}")
    print(f" computer first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      #tell that the game is over
      game_over = True 
    else: #if game has not ended, or no one got a blackjack, then this happens:
      user_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_another_card == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  #The computer now plays:
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards) #to update the computer's current score 
    
  print(f"   Your final hand is {user_cards}, your final score is {user_score}  ")
  print(f"   Computer's final hand is {computer_cards}, computer's final score is {computer_score}"  )
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game() #put everything into a single function so that the whole game gets repeated if user press 'y'