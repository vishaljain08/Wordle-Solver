discardedLetters = []

def checkInt(num):
    try:
        val = int(num)
        return True
    except ValueError:
        return False

def addDiscarded ():
    discardedLetters = []
    usrInp = input("Enter the discarded letters seeparated by a space >> ").upper()
    discardedLetters = discardedLetters + (usrInp.split())
    return discardedLetters

def checkDiscardedLetters(words, discardedLetters):
    potentialWords = []
    for word in words:
        if not any(letter in discardedLetters for letter in word):
            potentialWords.append(word)
    return potentialWords

def getGreenPositions():
    GreenPositions = []
    decision = True
    while True:
        userIn = input("Do you know any green positions? (y/n) ")
        if userIn.lower() == "n":
            decision = False
            break
        elif userIn.lower() == "y":
            decision = True
            break
        else: print ("Wrong Input")
    while decision == True:
        while True:
            x = input("Enter a green position you know ")
            if checkInt(x) == True:
                break
        x = int(x)-1
        while True:
            letter = input("Enter the letter in that posititon ").upper()
            if len(letter) == 1:
                break
        GreenPositions = GreenPositions + [str(letter) + " " + str(x)]
        while True:
            userIn = input("Know more GreenPositions? y/n ")
            if userIn.lower() == "n":
                decision = False
                break
            elif userIn.lower() == "y":
                decision = True
                break
            else: print ("Wrong Input")
    return GreenPositions


def checkGreenPositions(GreenPositions, words):
    if len(GreenPositions) == 0:
        return words 
    potentialWords = []
    potential = True
    for word in words:
        for keyValue in GreenPositions:
            key, value = keyValue.split()
            if word[int(value)] == key:
                potential = True
                continue
            else:
                potential = False
                break
        if potential == True:
            potentialWords.append(word)
    return potentialWords

def addYellowPositions ():
    YellowPositions = {}
    decision = True
    while True:
        userIn = input("Do you know any yellow positions? (y/n) ")
        if userIn.lower() == "n":
            decision = False
            break
        elif userIn.lower() == "y":
            decision = True
            break
        else: print ("Wrong Input")
    
    while decision == True:
        while True:
            x = input("Enter a yellow position you know ")
            if checkInt(x) == True:
                break
        x = int(x)-1
        while True:
            letter = input("Enter the letter in that posititon ").upper()
            if len(letter) == 1:
                break
        YellowPositions[letter] = x
        while True:
            userIn = input("Know more Yellow Positions? y/n ")
            if userIn.lower() == "n":
                decision = False
                break
            elif userIn.lower() == "y":
                decision = True
                break
            else: print ("Wrong Input")
    return YellowPositions

def checkYellowPositions(YellowPositions, words):
    if len(YellowPositions) == 0:
        return words
    potentialWords = []
    keys = list(YellowPositions.keys())
    values = list(YellowPositions.values())
    for word in words:
        if all(key in word for key in keys):
            potentialWords.append(word)
    for i in range(len(keys)):
        for word in potentialWords:
            if word[int(values[i])] == keys[i]:
                potentialWords.remove(word)

    return potentialWords


file = open("newWords.txt", "r")

words = file.read()
words = words.upper()
words = words.split()
file.close()
potentialWords = words
discardedLetters = []
GreenPositions = []
YellowPositions = {}

main = True
while main == True:

    discardedLetters = discardedLetters + addDiscarded()
    potentialWords = checkDiscardedLetters(potentialWords, discardedLetters)
    GreenPositions = GreenPositions + getGreenPositions()
    potentialWords = checkGreenPositions(GreenPositions, potentialWords)
    YellowPositions.update(addYellowPositions())
    potentialWords = checkYellowPositions(YellowPositions, potentialWords)
    

    print ("Top choice(s):")
    if len(potentialWords) < 5:
        print (*potentialWords, sep='\n')
    else:
        for i in range(-1,-5,-1):
            print (potentialWords[i])

    userInput = input("Completed? (y/n) ")
    while True:
        if userInput.lower() == "y":
            print ("Congrats")
            main = False
            break
        elif userInput.lower() == "n":
            main == True
            break
        else:
            print("Wrong input")


