#pyton is based on english, variables are in english, comments are in english
#it just makes sense

import random
import os
import time

#Random variables, refer to name
location = 1
bal = 100
balstr = str(bal) + "$"
timesplayed = 0
number = 0
if timesplayed == 0:
	firsttime = " first"


#Used for blackjack
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

#Used for dice animation
die     = ["   \n O \n   "]   
die.append("  O\n   \nO  ")   
die.append("O  \n O \n  O")   
die.append("O O\n   \nO O")  
die.append("O O\n O \nO O")   
die.append("O O\nO O\nO O")   


#_________________________ GENERAL _____________________________
#First thing that appears, simple instrutions and automatically sends you to next room
def start(bal) :

	global location

	print("""
	
	Welcome to the Casino!
	You have a balance of {}

	Today you'll be playing a variation of casino games
	with the goal of doubling your cash

	blackjacks availible:
	• Roulette (optionally with a twist)
	• blackjack
	• Slots
	• Baccarat 

	This is your {}th time playing

	""".format(balstr, timesplayed))
	location = 1
	position(bal)

#Area used for selection of what to play, reached by the newRound function
def position(bal) :
	
	if location == 1 :
		print("""

			Where should we go{}?

			You have: {}$
			
			Choose a room:

			_________________________
			│          Dice         │ 
			│                       │ 
			│Blackjack  x   Roulette│
			│                       │             
			│        Baccarat       │ 
			-------------------------
		""".format(firsttime,bal))
		where2go = input("Where should we go first?: ")
		cleanw2g = where2go.upper()
		if cleanw2g == "DICE" :
			dice(bal)
		elif cleanw2g == "BLACKJACK" :
			blackjack(bal)
		elif cleanw2g == "ROULETTE" :
			rouletteStart(bal)
		elif cleanw2g == "BACCARAT" :
			print("No one likes Baccarat")
			newRound(bal)

			
#Used to send player back after ending a round
def newRound(bal):
	again = input("Do you want to play again? (Y/N): ").lower()
	if again == "y":
		position(bal)


#Clears terminal for clarity purposes
def clear():
	os.system("cls")

#__________________________________ GENERALS END ______________________________	
# _________________________________ DICE ______________________________________

#Pretty much whole dice roll game, needs bal input because i removed global :(
def dice(bal) :
	#global :D
	global WonNumber
	usrbetint = 0
	#Print function with ascii art
	userbet = input(r"""\ 

(for help type help)  
	
                                                                                                                                               
I8,        8        ,8I          88                                                                    88888888ba,   88                        
`8b       d8b       d8'          88                                                ,d                  88      `"8b  ""                        
 "8,     ,8"8,     ,8"           88                                                88                  88        `8b                           
  Y8     8P Y8     8P  ,adPPYba, 88  ,adPPYba,  ,adPPYba,  88,dPYba,,adPYba,     MM88MMM ,adPPYba,     88         88 88  ,adPPYba,  ,adPPYba,  
  `8b   d8' `8b   d8' a8P_____88 88 a8"     "" a8"     "8a 88P'   "88"    "8a      88   a8"     "8a    88         88 88 a8"     "" a8P_____88  
   `8a a8'   `8a a8'  8PP        88 8b         8b       d8 88      88      88      88   8b       d8    88         8P 88 8b         8PP         
    `8a8'     `8a8'   "8b,   ,aa 88 "8a,   ,aa "8a,   ,a8" 88      88      88      88,  "8a,   ,a8"    88      .a8P  88 "8a,   ,aa "8b,   ,aa  
     `8'       `8'     `"Ybbd8"' 88  `"Ybbd8"'  `"YbbdP"'  88      88      88      "Y888 `"YbbdP"'     88888888Y"'   88  `"Ybbd8"'  `"Ybbd8"'  
                                                                                                                                               
                                                   
How much bal do you want to bet?
> """).upper()

	#Simple input-if setup for getting instrcutions or choosing bet amount
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

	#Calls the dice roll animation
	diceAnimation(number,usrnummer) 

	# print(WonNumber,usrnummer) testing purposes
	if WonNumber == usrnummer :
		usrbetint*=4
		bal += usrbetint
		print("\nCongrats, you won! \n\nYour new balance is {}".format(bal))
		newRound(bal)
	else :
		bal -= usrbetint
		print("\nSorry, you lost :( \n\nYour new balance is {}".format(bal))
		newRound(bal)
	
#Dice roll animation by printing out random combinations of o's from the list at the top
def diceAnimation(number,usrnummer):
	global WonNumber
	for roll in range(0,10):
		clear()
		print("\n")
		number = random.randint(0,5)
		print(die[number])
		time.sleep(0.3)
		if roll == 9 :
			WonNumber = number+1
			print("Your final roll was:", WonNumber)
			print("You chose: {}".format(usrnummer))
	return(number,WonNumber)

#______________________________ DICE END ____________________________________
#______________________________ blackjack ___________________________________

#Gives both the player and the dealer their decks, both are treated the same way
#with the dealer just being controlled by predetermined conditions
#(would be very simple to add another a player)
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

#Since some values are defined as letters we have to have this funciton to
#give a way of counting the hands as int values
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

#Like dealing but just with one card kinda, used by both player and dealer
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

#Print statement with totals
def currentHands(dealerHand, playerHand):
	clear()
	print(("The dealer has a ") + str(dealerHand) + " for a total of " + str(total(dealerHand)))
	print(("You have a ") + str(playerHand) + " for a total of " + str(total(playerHand)))

#Used to decide who won, equal means player wins which isnt how it works in real blackjack but whatever
def score(dealerHand, playerHand, usrbetint, bal):

	if total(playerHand) == 21 or total(dealerHand) > 21 or total(playerHand) > total(dealerHand) and total(playerHand) < 21:
		currentHands(dealerHand, playerHand)
		bal += usrbetint
		print("Congratulations, you win!\n \nYour new balance is {}$".format(bal))
		newRound(bal)
	else :
		currentHands(dealerHand, playerHand)
		bal -= usrbetint		
		print("Sorry, you lose.\n \nYour new balance is {}$".format(bal))
		newRound(bal)

#Pretty much just letting the players interact with above defined functions 	
def blackjack(bal):
	choice = 0
	clear()
	print(r"""
	
	                                                                                                                                                                    
888888888888 88                                     ad88                          88888888ba  88                       88        88                       88         
     88      ""                                    d8"                            88      "8b 88                       88        ""                       88         
     88                                            88                             88      ,8P 88                       88                                 88         
     88      88 88,dPYba,,adPYba,   ,adPPYba,    MM88MMM ,adPPYba,  8b,dPPYba,    88aaaaaa8P' 88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
     88      88 88P'   "88"    "8a a8P_____88      88   a8"     "8a 88P'   "Y8    88       8b, 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
     88      88 88      88      88 8PP"            88   8b       d8 88            88      `8b 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
     88      88 88      88      88 "8b,   ,aa      88   "8a,   ,a8" 88            88      a8P 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
     88      88 88      88      88  `"Ybbd8"'      88    `"YbbdP"'  88            88888888P"  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                                                                                                                ,88                                  
                                                                                                                              888P"                 
	
	
	""")

	#Normal bet input
	userbet = input("(for help type help) How much bal do you want to use: ").upper()

	if userbet == "HELP" :
		if userbet == "HELP" :
			print("Instructions")
		else :
			print("Something went wrong")
			pass
	else :
		usrbetint = int(userbet)
	while usrbetint > bal:
		clear()
		print("You don't have enough bal.")
	#Application of the previously made functions and more print statements
	dealerHand = deal(deck)
	dealerHandShow = [dealerHand[0]]
	dealerHandShow = total(dealerHandShow)
	playerHand = deal(deck)
	print(("The dealer is showing a ") + str(dealerHand[0]) + " for a total of " + str(dealerHandShow))
	print("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))
	choice = input("Do you want to [H]it or [S]tand?: ").lower()
	#im aware that you get the chance to hit or stand when you already lost but inputing any choice in that state wont affect the result
	while choice == "h" and total(playerHand) != 21 and total(playerHand) < 21:
		clear()
		hit(playerHand)
		print(("The dealer is showing a ") + str(dealerHand[0]) + " for a total of " + str(dealerHandShow))
		print("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))
		choice = input("Do you want to [H]it or [S]tand?: ").lower()

	while total(dealerHand) < 17:
		hit(dealerHand)

	score(dealerHand, playerHand, usrbetint, bal)
#_________________________ BLACKJACK END _________________________
#_________________________ ROULETTE ______________________________

#No fancy functions for this one and the code is pretty much like dice
empty = False
def rouletteStart(bal) :
	print(r"""
	
                                                                                                                                                                   
88                                                     88                           88888888ba                         88                                       
88                      ,d                             88                           88      "8b                        88              ,d      ,d               
88                      88                             88                           88      ,8P                        88              88      88               
88          ,adPPYba, MM88MMM ,adPPYba,    8b,dPPYba,  88 ,adPPYYba, 8b       d8    88aaaaaa8P' ,adPPYba,  88       88 88  ,adPPYba, MM88MMM MM88MMM ,adPPYba,  
88         a8P_____88   88    I8[    ""    88P'    "8a 88 ""     `Y8 `8b     d8'    88    88'  a8"     "8a 88       88 88 a8P_____88   88      88   a8P_____88  
88         8PP          88     `"Y8ba,     88       d8 88 ,adPPPPP88  `8b   d8'     88    `8b  8b       d8 88       88 88 8PP          88      88   8PP  
88         "8b,   ,aa   88,   aa    ]8I    88b,   ,a8" 88 88,    ,88   `8b,d8'      88     `8b "8a,   ,a8" "8a,   ,a88 88 "8b,   ,aa   88,     88,  "8b,   ,aa  
88888888888 `"Ybbd8"'   "Y888 `"YbbdP"'    88`YbbdP"'  88 `"8bbdP"Y8     Y88'       88      `8b `"YbbdP"'   `"YbbdP'Y8 88  `"Ybbd8"'   "Y888   "Y888 `"Ybbd8"'  
                                           88                            d8'                                                                                    
                                           88                           d8'                   
	
	""")
	global VeryUsedGlobal
	startPrompt = input("What do you wanna do? (Tutorial, Start): ").lower()
	#Choice for instructions
	if startPrompt == "tutorial":
		print("Insrutions")
	else:
		clear()
		print("You have {}$".format(bal))
		roulette(bal)
	
#Split inte two because i planning on looping it another way at first 	
def roulette(bal) :
	#Bla bla bla bet
	print("How much do you want to bet?\n")
	clear()
	betNmrInt = int(input("Bet: "))
	clear()
	while betNmrInt > bal:
		print("\n")
		print("You don\'t have enough bal.")
		print("\n")
		betNmrInt = int(input("Bet: "))
	#Section about what you want to bet on (nummer or color)
	betType = input("Bet on what? Number or Color?: ").lower()
	if betType == "number" :
		rlNumber(bal,betNmrInt)
	elif betType == "color" :
		rlColor(bal,betNmrInt)

#Section for number roulette	
def rlNumber(bal,betNmrInt)	:
	finalBet = int(input("What number do you bet on?: "))
	if 1 <= finalBet <= 36:
		print("The roulette is spinning...")
		time.sleep(3)
		WinNmr = random.randint(1, 37)
		print("Number {} won\n".format(WinNmr))
	if WinNmr == finalBet:
		print("Congratulations!You've won 20 times your bet!")
		bal += betNmrInt * 20
		print("Your new balance is {}$".format(bal))
		time.sleep(2)			
		newRound(bal)
	else:
		print("Sorry, you lost, better luck next time!")
		bal -= betNmrInt
		print("Your new balance is {}$".format(bal))
		time.sleep(2)
		newRound(bal)

#Section for color roulette
def rlColor(bal,betNmrInt) :
	betColor = input("What color do you want to bet on? ").lower()
	if betColor == "black" or betColor == "red":
		print("The roulette is spinning...")
		time.sleep(3)
		WinNmr = random.choice(["red", "black"])
		print("The roulette lands on {}".format(WinNmr))
		if WinNmr == betColor:
			print("You win, you doubled your bet!")
			bal += betNmrInt
			print("Your new balance is {}$".format(bal))
			time.sleep(2)
			newRound(bal)
		else:
			print("Unfortunately, you\'ve lost this time. Hope you won next time!")
			bal -= betNmrInt
			print("Your new balance is {}$".format(bal))
			time.sleep(2)
			newRound(bal)

#will anyone notice if I just dont include baccarat?
#what even is baccarat
#i have 4 rooms anyway, no one would miss it

start(bal)