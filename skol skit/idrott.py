lag = 0
elever = ["melker","gustav","olaf","rickard"]
for x in elever:
    if (lag % 2) == 0:
        print(x, "är i lag 1")
        lag += 1
    else :
        print(x, "är i lag 2")
        lag += 1