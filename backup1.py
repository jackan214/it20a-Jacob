import random
import os
import time

location = 1
bal = 100
balstr = str(bal) + "$"
timesplayed = 0
number = 0
if timesplayed == 0:
	firsttime = " first"

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

die     = ["   \n O \n   "]   
die.append("  O\n   \nO  ")   
die.append("O  \n O \n  O")   
die.append("O O\n   \nO O")  
die.append("O O\n O \nO O")   
die.append("O O\nO O\nO O")   


def start() :

	global location

	print("""
	
	Welcome to the Casino!
	You have a balance of {}

	Today you'll be playing a variation of games
	with the goal of doubling your cash

	Games availible:
	• Roulette (optionally with a twist)
	• Blackjack
	• Slots
	• Baccarat 

	This is your {}th time playing

	""".format(balstr, timesplayed))
	location = 1
	position()


def position() :
	
	if location == 1 :
		print(""""

			Where should we go{}?
			
			Choose a room:

			_________________________
			│          Dice         │ 
			│                       │ 
			│Slotts     x  Blackjack│
			│                       │             
			│        Baccarat       │ 
			-------------------------
		""".format(firsttime))
		where2go = input("Where should we go first?: ")
		cleanw2g = where2go.upper()
		if cleanw2g == "DICE" :
			dice()
	
# _________________________________ DICE ______________________________________

def dice() :
	global bal
	
	usrbetint = 0
	userbet = input("(for help type help) How much money do you want to use: ")
	usrbetupper = userbet.upper()

	if usrbetupper == "HELP" :
		if usrbetupper == "HELP" :
			print("Instructions")
		else :
			print("Something went wrong")
			pass
	else :
		usrbetint = int(userbet)
	usrnummer = int(input("What nummer do you want to bet on? (1-6): "))
	for countdown in range(3,0,-1) :
		print("Die rolling in: ", countdown)
		time.sleep(0.8)

	diceAnimation() 

	print(number)
	print(usrnummer)

	if number+1 == usrnummer :
		usrbetint*4
		bal += usrbetint
		print("\nCongrats, you won! \n\nYour new balance is {}".format(bal))

	else :
		bal -= usrbetint
		print("\nSorry, you lost :( \n\nYour new balance is {}".format(bal))

	
	
def diceAnimation():
	global number
	for roll in range(0,10):
		os.system('cls')
		print("\n")
		number = random.randint(0,5)
		print(die[number])
		time.sleep(0.3)
		if roll == 9 :
			print("Your final roll was:", number+1)

#______________________________ DICE END ____________________________________
#______________________________ BLACKJACK ___________________________________


def deal(deck):
	hand = []
	for i in range(2):
		random.shuffle(deck)
		card = deck.pop()
		if card == 11:card = "J"
		if card == 12:card = "Q"
		if card == 13:card = "K"
		if card == 14:card = "A"
		hand.append(card)
	return hand

def play_again():
	again = input("Do you want to play again? (Y/N) : ").lower()
	if again == "y":
		dealerHand = []
		playerHand = []
		deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
		game()
	else:
		print("Bye!")
		exit()

def total(hand):
	total = 0
	for card in hand:
		if card == "J" or card == "Q" or card == "K":
			total+= 10
		elif card == "A":
			if total >= 11: total+= 1
			else: total+= 11
		else:
			total += card
	return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def clear():
	os.system('cls')

def print_results(dealerHand, playerHand):
	clear()
	print("The dealer has a ") + str(dealerHand) + " for a total of " + str(total(dealerHand))
	print("You have a ") + str(playerHand) + " for a total of " + str(total(playerHand))

def blackjack(dealerHand, playerHand):
	if total(playerHand) == 21:
		print_results(dealerHand, playerHand)
		print("Congratulations! You got a Blackjack!\n")
		play_again()
	elif total(dealerHand) == 21:
		print_results(dealerHand, playerHand)		
		print("Sorry, you lose. The dealer got a blackjack.\n")
		play_again()

def score(dealerHand, playerHand):
	if total(playerHand) == 21:
		print_results(dealerHand, playerHand)
		print("Congratulations! You got a Blackjack!\n")
	elif total(dealerHand) == 21:
		print_results(dealerHand, playerHand)		
		print("Sorry, you lose. The dealer got a blackjack.\n")
	elif total(playerHand) > 21:
		print_results(dealerHand, playerHand)
		print("Sorry. You busted. You lose.\n")
	elif total(dealerHand) > 21:
		print_results(dealerHand, playerHand)			   
		print("Dealer busts. You win!\n")
	elif total(playerHand) < total(dealerHand):
		print_results(dealerHand, playerHand)
		print("Sorry. Your score isn't higher than the dealer. You lose.\n")
	elif total(playerHand) > total(dealerHand):
		print_results(dealerHand, playerHand)			   
		print("Congratulations. Your score is higher than the dealer. You win\n")		

def game():
	choice = 0
	clear()
	print("Let's play blackjack!\n")
	dealerHand = deal(deck)
	playerHand = deal(deck)
	while choice != "q":
		print(("The dealer is showing a ") + str(dealerHand[0]))
		print(("You have a ") + str(playerHand) + " for a total of " + str(total(playerHand)))
		blackjack(dealerHand, playerHand)
		choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
		clear()
		if choice == "h":
			hit(playerHand)
			while total(dealerHand) < 17:
				hit(dealerHand)
			score(dealerHand, playerHand)
			play_again()
		elif choice == "s":
			while total(dealerHand) < 17:
				hit(dealerHand)
			score(dealerHand, playerHand)
			play_again()
		elif choice == "q":
			print("Bye!")
			exit()

game()