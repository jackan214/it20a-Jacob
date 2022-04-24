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

#_________________________ GLOBALS ___________________________
def start() :

	global location

	print("""
	
	Welcome to the Casino!
	You have a balance of {}

	Today you'll be playing a variation of blackjacks
	with the goal of doubling your cash

	blackjacks availible:
	• Roulette (optionally with a twist)
	• Blackjack
	• Slots
	• Baccarat 

	This is your {}th time playing

	""".format(balstr, timesplayed))
	location = 1
	position()


def position() :
	global bal
	
	if location == 1 :
		print("""

			Where should we go{}?

			You have: {}$
			
			Choose a room:

			_________________________
			│          Dice         │ 
			│                       │ 
			│Slotts     x  Blackjack│
			│                       │             
			│        Baccarat       │ 
			-------------------------
		""".format(firsttime,bal))
		where2go = input("Where should we go first?: ")
		cleanw2g = where2go.upper()
		if cleanw2g == "DICE" :
			dice()
		elif cleanw2g == "BLACKJACK" :
			blackjack()

def clear():
	os.system('cls')

#__________________________________ GLOBALS END _______________________________________	
# _________________________________ DICE ______________________________________

def dice() :
	global bal
	
	usrbetint = 0
	userbet = input("(for help type help) How much money do you want to use: ").upper()

	if userbet == "HELP" :
		if userbet == "HELP" :
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

	diceAnimation(number) 

	if number+1 == usrnummer :
		usrbetint*4
		bal += usrbetint
		print("\nCongrats, you won! \n\nYour new balance is {}".format(bal))

	else :
		bal -= usrbetint
		print("\nSorry, you lost :( \n\nYour new balance is {}".format(bal))
	
def diceAnimation(number):
	for roll in range(0,10):
		clear()
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

def newRound():
	again = input("Do you want to play again? (Y/N): ").lower()
	if again == "y":
		blackjack()
	else:
		position()

def total(hand):
	total = 0
	for card in hand:
		if card == "J" or card == "Q" or card == "K":
			total+= 10
		elif card == "A":
			if total >= 11: 
				total+= 1
			else: total+= 11
		else:
			total += card
	return total

def hit(hand):
	card = deck.pop()
	if card == 11:
		card = "J"
	if card == 12:
		card = "Q"
	if card == 13:
		card = "K"
	if card == 14:
		card = "A"
	hand.append(card)
	return hand

def currentHands(dealerHand, playerHand):
	clear()
	print(("The dealer has a ") + str(dealerHand) + " for a total of " + str(total(dealerHand)))
	print(("You have a ") + str(playerHand) + " for a total of " + str(total(playerHand)))

def score(dealerHand, playerHand, usrbetint):
	global bal

	if total(playerHand) > 21 and total(playerHand) > 21 :
		print("Both failed, no effect on points")
		currentHands(dealerHand, playerHand)
		#orkar inte fixa det här så bara hoppas att det inte händer
	elif total(playerHand) == 21 or total(dealerHand) > 21 or total(playerHand) > total(dealerHand) and total(playerHand) < 21:
		currentHands(dealerHand, playerHand)
		bal += usrbetint
		print("Congratulations, you win!\n \nYour new balance is {}$".format(bal))
	else :
		currentHands(dealerHand, playerHand)
		bal -= usrbetint		
		print("Sorry, you lose.\n \nYour new balance is {}$".format(bal))

	
def blackjack():
	choice = 0
	clear()
	print("Let's play blackjack!\n")
	userbet = input("(for help type help) How much money do you want to use: ").upper()
	if userbet == "HELP" :
		if userbet == "HELP" :
			print("Instructions")
		else :
			print("Something went wrong")
			pass
	else :
		usrbetint = int(userbet)
	dealerHand = deal(deck)
	dealerHandShow = [dealerHand[0]]
	dealerHandShow = total(dealerHandShow)
	playerHand = deal(deck)
	print(("The dealer is showing a ") + str(dealerHand[0]) + " for a total of " + str(dealerHandShow))
	print("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))
	choice = input("Do you want to [H]it or [S]tand?: ").lower()
	while choice == "h" :
		clear()
		hit(playerHand)
		print("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))
		if total(playerHand) == 21 or total(playerHand) > 21 :
			break
		choice = input("Do you want to [H]it or [S]tand?: ").lower()

	while total(dealerHand) < 17:
		hit(dealerHand)

	score(dealerHand, playerHand, usrbetint)


	# print(("You have a ") + str(playerHand) + " for a total of " + str(total(playerHand)))
	# choice = input("Do you want to [H]it or [S]tand?: ").lower()
	# clear()
	# if choice == "h":
	# 	hit(playerHand)
	# 	while total(dealerHand) < 17:
	# 		hit(dealerHand)
	# 	score(dealerHand, playerHand, usrbetint)
	# 	newRound()
	# elif choice == "s":
	# 	while total(dealerHand) < 17:
	# 		hit(dealerHand)
	# 	score(dealerHand, playerHand, usrbetint)
	# 	newRound()

start()