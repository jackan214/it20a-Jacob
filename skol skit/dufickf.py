while (True) :
    grade = int(input("What was your score?:"))
    """
    A = 43
    C = 30
    E = 25
    """
    if grade>=51 :
        print("Too high score!")
    elif grade>=43 :
        print("Jag såg att du kopierade från Jacob, du fick A")
    elif grade>=30 :
        print("Har roligt på bygg, du fick bara C")
    elif grade>=25 :
        print("Vill du ha en applåd eller? du fick E")
    else :
        print("Stackaras tappade unge, du fick F")