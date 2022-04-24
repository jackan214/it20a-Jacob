from random import randint
from random import sample

players = ["Jacob ", "Hugo ", "Eddie ", "Viktor ", "Monir ", "Darin ", "Melker ", "Melvin ", "Hugo ", "Anton ", "Sebastian ", "Flamur ", "Erik ", "Oscar ", "Oskar ", "Jonathan ", "Oliver ", "William ", "Melvin ", "Pelle ", "Mario ", "Robin ", "Vilgot "]

def game() :
    
    Game = randint(0,1)
    if Game == 1 :
        Game = "Lantbruk"
    else :
        Game = "Tvärtom quiz"

    print("\nThe game we're playing is:", Game)

    winners = sample(players,3)
    needcomma = x=winners[0]
    if needcomma == "Hugo " :
        hugonr = randint(0,1)
        if hugonr == 1 :
            hascomma = needcomma.replace(" "," H, ")
        else :
            hascomma = needcomma.replace(" "," C, ")
    else : hascomma = hascomma = needcomma.replace(" ",", ")


    winners.insert(2,"and ")
    winners[0]=hascomma
    winnersstr = "".join(winners)

    print("\nThe winners were:\n"+winnersstr, "\n")


game()