def correctcheck(test) :
    if income <= 120000 :
        print("Tyvärr kan vi inte bevilja din faktura betalning")
        quit()
    elif age < 18 :
        print("Tyvärr kan vi inte bevilja din faktura betalning")
        quit()
    elif mark >= 1 :
        print("Tyvärr kan vi inte bevilja din faktura betalning")
        quit()
       


income = input(print("Vad är din lön?: "))
correctcheck
age = input(print("Hur gammal är du?: "))
correctcheck
mark = input(print("Har du några kreditanmärkningar?: "))
correctcheck
print("Grattis")