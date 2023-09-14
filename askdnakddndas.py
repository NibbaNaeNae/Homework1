class Deck:
    def __init__(self, name="", length=0, width=0, cost=0):
        self.name = name
        self.length = length
        self.width = width
        self.cost = cost

def read_file_data(array):
    with open('info.csv', 'r') as f:
        counter = 0
        for line in f:
            items = line.strip().split(",")
            array.append(Deck(items[0], float(items[1]), float(items[2]), int(items[3])))
            counter += 1

def find_cheapest(array):
    if not array:
        return None

    minimum = array[0].cost
    minimum_pos = 0

    for x in range(1, len(array)):
        if array[x].cost < minimum:
            minimum = array[x].cost
            minimum_pos = x

    return minimum_pos

def display_decks_over_length(array, min_length):
    for deck in array:
        if deck.length > min_length:
            print(deck.name)

def count_decks_over_area(array, min_area):
    count = 0
    for deck in array:
        if deck.length * deck.width > min_area:
            count += 1
    print("Number of garden decks available over a certain area:", count)

def get_user_input():
    decks = []
    read_file_data(decks)

    while True:
        menu_prompt = input("Enter 1 to find the cheapest garden deck\n"
                            "Enter 2 to display the names of the garden decks over a certain length\n"
                            "Enter 3 to display the number of garden decks that are available over a certain area\n"
                            "Enter 4 to quit\n")

        if menu_prompt == '1':
            cheapest_pos = find_cheapest(decks)
            if cheapest_pos is not None:
                print("The cheapest deck is", decks[cheapest_pos].name)
            else:
                print("No decks available.")

        elif menu_prompt == '2':
            min_length = float(input("Enter the minimum length: "))
            display_decks_over_length(decks, min_length)

        elif menu_prompt == '3':
            min_area = float(input("Enter the minimum area: "))
            count_decks_over_area(decks, min_area)

        elif menu_prompt == '4':
            break

        else:
            print("Invalid input. Please try again.")

get_user_input()
