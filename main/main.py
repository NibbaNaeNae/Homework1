class deck:
    name:str = ""
    length:float = 0
    width:float = 0
    cost:int = 0

def readFileData(array):
    with open('info.csv', 'r') as f:
        line = f.readline().rstrip("\n")
        counter = 0
        while line:
            items = line.split(",")
            array[counter].name = items[0]
            array[counter].length = float(items[1])
            array[counter].width = float(items[2])
            array[counter].cost = int(items[3])

            counter = counter + 1 
            line = f.readline().rstrip("\n")

def findCheapest(array):
    minimum = array[0].cost
    minimumPos = 0

    for x in range (0,len(array)):
        if array[x].cost < minimum:
            minimum = array[x].cost
            minimumPos = x
            print("The cheapest deck is " + minimum)

        return minimum, minimumPos

decks = deck()
readFileData(decks)

def getUserInput():
    menuPrompt = int(input("Enter 1 to find the cheapest garden deck\nEnter 2 to display the names of the garden decks over a certain length\nEnter 3 to display the number of garden decks that are available over a certain area\nEnter 4 to quit"))
    if menuPrompt == 1:
        findCheapest(decks)
    else:
        print("problem bruh")

getUserInput()
