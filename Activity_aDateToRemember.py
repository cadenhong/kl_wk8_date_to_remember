# A Date to Remember!

def separator():
    print("------------------------------------------------------------")

#you = input("Enter your name: ")
#date = input("Enter your date's name: ")
caden = "Caden"
casey = "Casey"
restaurant = "Kura Diner"
feelings = ['Bored', 'Uninterested', 'Intrigued', 'Interested']
menu = {'Salads': ['Grilled Chicken Salad', 'Mixed Baby Greens', 'Quinoa Salad with Salmon'], 'Burgers and Sandwiches': ['Classic Burger', 'Veggie Burger', 'Chicken Sandwich'], 'Sides': ['Fries', 'Wings', 'Coleslaw']}
price = {'Salads': 20, 'Burgers and Sandwiches': 25, 'Sides': 15}

separator()
print(f'A Date To Remember at {restaurant}'.center(60))
separator()
print(f'Hi {caden} and {casey}! Welcome to {restaurant}!\nHope you lovebirds have a great time!')
money = int(input("Please enter how much money you brought for tonight: "))

if money < 30:
    separator()
    print('Sorry... You don\'t have enough to dine here tonight')
else:
    print(f'\nHere is the menu:\n')
    for item in menu:
        print(item)

    cadenCategory = input("\nWhich would you like to choose from? ")
    cadenItem = input(f'Excellent choice! Choose an item from the list: {menu[cadenCategory.capitalize()]}: ')
    caseyCategory = input(f'\nWhat about you, {casey}? Which would you like to choose from? ')
    caseyItem = input(f'Awesome! Choose an item from the list: {menu[caseyCategory.capitalize()]}: ')

    status = input(f'\nAn order of {cadenItem} for {caden}, and {caseyItem} for {casey}! So {caden}, how is the date going so far? Choose from this list: {feelings}: ')

    payer = input(f'\nOkay, time to pay... Who\'s paying? ')
    total = price[cadenCategory] + price[caseyCategory]
    money = money - total

    print(f'{payer} bill came out to ${total} - you now have ${money} left')

    if status.capitalize() == 'Bored' or status.capitalize() == 'Uninterested':
        if cadenCategory.capitalize() == 'Sides' or caseyCategory.capitalize() == 'Sides':
            print('Sorry, there won\'t be a next date...')
    elif status.capitalize() == 'Intrigued':
        if cadenCategory.capitalize() == 'Sides' or caseyCategory.capitalize() == 'Sides':
            print('Sorry, there won\'t be a next date...')
        elif cadenCategory.capitalize() == 'Salads' or caseyCategory.capitalize() == 'Salads':
            print('Hmm... Maybe there\'s a chance... Try hitting them up in a couple of days!')
        else:
            print('Wooo! Successful date! Definitely set up a second date!')
    else:
        print('Wooo! Successful date! Definitely set up a second date!')