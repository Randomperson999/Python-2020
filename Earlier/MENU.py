def get_menu_choice():
    options = ["Burger, Fries, Soda", "Chicken Salad, Iced Tea", "Pizza, Soda"]
    cost = [6.99, 10.50, 5.72]

    print("Your menu choices are: ")
    for i in range(len(options)):
        print(str.format("{} - ${:5.2f} : {}", i+1, cost[i], options[i]))

    choice = ask_number("What will you have?: ",0,len(options)+1)

    order = options[choice-1]
    price = cost[choice-1]
    taxRate = .075
    total = price + (taxRate*price)

    print(str.format("O K  you have ordered ----- {}", order))
    print(str.format("Out the door you are looking at ----- ${:5.2f}", total))
def ask_number(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
def ask_y_or_n(question):
    """Ask a yes or no question. Only returns yes or no"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
running = "y"
while running == "y":
    get_menu_choice()
    running = ask_y_or_n("You want to order M O R E?")
