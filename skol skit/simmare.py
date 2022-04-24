import random

difficulty = int(input("What was the difficulty of this game? (1-10, int only): "))
judgesValues = []
judgesAmount = random.randint(5,10)
for i in range(0,judgesAmount):
    n = random.randint(1,30)
    judgesValues.append(n)

judgesAmount -= 2
judgesValues = sorted(judgesValues)

del judgesValues[0]
del judgesValues[-1]

finalValue = 0

#print(judgesValues)

for i in judgesValues :
    finalValue += i

# print(finalValue,"   ", judgesAmount)
finalValue /= judgesAmount
#print(finalValue)

finalValue *= 3
finalValue *= difficulty

print("The result of this jump was:", finalValue, "\nThere were", judgesAmount, "judges \nThey rated you", judgesValues)