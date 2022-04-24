list1 = []
    
antalElement = int(input("hur många element ska du ha i din lista: "))

for i in range(1, antalElement + 1) :
    element = int(input("skriv in dina element är du snäll: "))
    list1.append(element)

list1.sort()


notbiggest = []

for x in list1 :
    if x == list1[0] :
        continue
    else :
        notbiggest.clear()
        notbiggest.append(x)

global everything

print("Det näst största elementet är", notbiggest)