helo = 1

def hello() :
    global helo
    helo += 2

hello()
print(helo)