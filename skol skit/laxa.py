#Frågar användaren att svara på två frågar som definerar variablerna "FavoriteAnimal", "FavoriteFood", och "SomeNumber"
FavoriteAnimal = input("Whats your favorite animal?:")
FavoriteFood = input("Whats your favorite food?:")
SomeNumber = input("Say a number:")

#Skriver ut variableran "FavoriteAnimal" och "FavoriteFood" med komma, blanksteg imellan, och en bit text först
print("your favorite animal and food is:", FavoriteAnimal+", "+FavoriteFood)

#Provar datatypen på variabeln "SomeNumber"
print("Your SomeNumber input was the class:")
print(type(SomeNumber))

#Ändrar typen på "SomeNumber" till integer, byter också variabelns namn
SomeNumberButItsAnIntegerNow=int(SomeNumber)

#Provar datatypen på variabeln "SomeNumber" igen med ny class
print("Your SomeNumber input was the class:")
print(type(SomeNumberButItsAnIntegerNow))
