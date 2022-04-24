#Hämtar random så vi kan använda detta senare
import random

#Sätter variabeln till 0, vi måste ha denna utanför loopen så det inte återställs varje gång
Winningstreak = 0
#Definerar de olika subjekten som spelaren kommer gissa på, denna hade kunnat vara i 
#loopen men det spelar ingen roll
Element = ["Volvo", "Audi", "pornhub", "mygga", "golf", "apple", "suicide"]

#definerar programmet så vi kan ha simplare loopar och kunna expandera koden enklare senare
def program() :
    #Hämtar variabeln winningstreak och låter oss redigera den inom funktionen, 
    #utan detta kommandot hade vi inte kunnat röra värdet
    global Winningstreak
    
    #Väljer ett slumpat subjekt från listan jag skrev innan
    value = random.choice(Element)

    #Bestämmer värdet på subjektet och definerar räckvidden för rätt svar
    ElementValue = random.randint(0, 200000)
    EValueRange1 = ElementValue + 10000
    EValueRange2 = ElementValue - 10000

    #For testing reasons
    print(ElementValue) 


    #Skriver ut start prompten och vi var tvungna att använda .format istället
    #för det enklare sättet med ", UserResponse, "
    print("Vad tror du {} har för popularitetsvärde? ". format(value))
    #Sparar svaret från användaren i UserResponse, accepterar bara integers
    UserResponse = int(input("Skriv ett värde mellan 0 och 200,000: "))

    #Först provar användarens input för rätt svar och i så fall ökar winningstreak 
    #med ett och skriver ut ett meddelande, efter börjar det om igen
    if UserResponse >= EValueRange2 and UserResponse <= EValueRange1 :
        Winningstreak = Winningstreak + 1

        print("\nGrattis du vann! \nRätt svar var {} \n".format (ElementValue))
        print("Du har en winningstreak på: ", Winningstreak, "\n")
    #I alla andra fall så skickas man funktionen "loss" vilket inte är dålig meme 
    #från 2018 utan en fråga om du vill ge upp eller fortsätta
    else :
        print("Tyvärr, du förlorade. Jävla sopa, rätt svar var {}".format (ElementValue))
        loss()

#Definerar funktionen loss för när man skriver fel svar
def loss() :
    KeepPlaying = input('Vill du fortsätta? [Y, N] : ')
    if KeepPlaying == "N" :
        quit()

#Loopar programmet, om användaren har svarat nej på loss så avslutas programmet innan 
#det kommer hit
while (True) :
    program()