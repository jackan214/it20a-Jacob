print("Ge mig två nummer så jag kan dela dem")
print("Skriv in Q för att sluta")
answer = ""
while True :
    nummer1 = input("Första nummer: ")
    if nummer1 == "Q" :
        pass
    else :
        nummer1f = float(nummer1)

    nummer2 = float(input("Andra nummret: "))
    try :
        answer = nummer1f/nummer2
    except ZeroDivisionError :
        print("Du kan inte dela med noll")
        pass
    print(answer)