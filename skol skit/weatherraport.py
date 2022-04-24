import random
seeds = 0
#hämtar vädret och temperaturen
# 1= Sol, 2= Klart(inte regn) 3= Blåsigt 4= Snö
weather = random.randint(1,4)
Temp = random.randint(-20,40)
#skriver ut för felsökningsanledningar 
print(Temp)
print(weather)
#om det är över 20 grader och soligt
if Temp >= 20 and weather == 1 :
    seeds = 5
    print("""
    Vad gör tandläkaren på lunchen?

    Käkar!
    """)
#om det är blåsigt eller exakt 20 grader
elif Temp == 20 or weather == 3 :
    print("Radio är igång")
#dessa 2 under är om det snöar eller är minusgrader men jag glömde använde "or"
elif Temp <= 0 :
    seeds = random.randint(1,824091430831412)
elif weather == 4 :
    seeds = random.randint(1,824091430831412)
#Sista kvar är imellan 0-20 när det inte regnar(gav det nmr 2 för enkelhetens skull), satte den sist
#pga att den långa texten ser dålig ut mitt i
else :
    seeds = 10
    print("""
När vi går genom staden över broar och torg
Med doft av salt ifrån havet minns vi glädje och sorg
Och vi minns första gången när änglarna sjöng
Hur vårsolen värmde och vintern var glömd

Åh, när vi kastar våra tomma glas
Finns det alltid någon med hjärtat kvar
Födda ur hav och himmel står vi kvar
För vi glömmer aldrig denna stad

Vi såg hur du haltade, vi såg hur du sprang
Med tårar på kinden och hjärtat i brand
Med längtan i bröstet, du stod där och sa:
"Snart skiner Poseidon och Blåvitt står kvar"

Åh, när vi kastar våra tomma glas
Finns det alltid någon med hjärtat kvar
Födda ur hav och himmel står vi kvar
För vi glömmer aldrig Änglarna
""")
#skriver up mängden frön
print("Idag ska du äta: ", seeds)