# A Date to Remember!

import random

def separator():
    print("------------------------------------------------------------")

user = "Caden"
date = "Casey"
restaurant = "Kura Diner"
feelings = ['Bored', 'Uninterested', 'Intrigued', 'Interested']
menu = {'Salad': ['Chicken', 'Green', 'Quinoa'], 'Burger': ['Classic', 'Veggie', 'Bean'], 'Side': ['Fries', 'Wings', 'Coleslaw']}
price = {'Salad': 20, 'Burger': 25, 'Side': 15}

separator()
print(f'A Date To Remember at {restaurant}'.center(60))
separator()
print(f'Hi {user} and {date}! Welcome to {restaurant}!\nHope you lovebirds have a great time!\n')
money = float(input("Enter how much money you brought for tonight: $"))

if money < 30:
    separator()
    print('Sorry, the minimum is $30 - you don\'t have enough to dine here tonight')
    separator()
else:
    separator()
    print(f'Here is the menu:\n')
    for item in menu:
        print(f'{item}, ${price[item]}'.center(60))

    while True:
        userCategory = input("\nWhich category would you like to choose from? ")
        checkUserInput = menu.get(userCategory.capitalize())
        if checkUserInput is not None:
            while True:
                userItem = input(f'\nChoose an item from {menu[userCategory.capitalize()]}: ')
                if userItem in menu[userCategory.capitalize()]:
                    break
                else:
                    print("Invalid category!")
            break
        else:
            print(f'Invalid category! Select from {menu.keys()}!')

    dateCategory = random.choice(list(menu.keys()))
    dateRandom = random.randint(0,2)
    dateItem = menu[dateCategory][dateRandom]

    status = input(f'\nAn order of {userItem} for {user}, and {dateItem} for {date}!\n\n*Whisper*So {user}, how is the date going so far? Choose from this list: {feelings}: ')

    separator()

    total = price[userCategory] + price[dateCategory]
    money = money - total

    print(f'Hope you enjoyed your meals. Your total bill comes out to ${total}')
    
    if money < 0:
        print(f'\nYour card got declined - there\'s not enough money, the balance is ${money}')
    else:
        print(f'\nThanks for the payment, {user}! You now have ${money} left')

        if status.capitalize() == 'Bored' or status.capitalize() == 'Uninterested':
            if userCategory.capitalize() == 'Sides' or dateCategory.capitalize() == 'Sides':
                print('Sorry, there won\'t be a next date...')
        elif status.capitalize() == 'Intrigued':
            if userCategory.capitalize() == 'Sides' or dateCategory.capitalize() == 'Sides':
                print('Sorry, there won\'t be a next date...')
            elif userCategory.capitalize() == 'Salads' or dateCategory.capitalize() == 'Salads':
                print('Hmm... Maybe there\'s a chance... Try hitting them up in a couple of days!')
            else:
                print('Wooo! Successful date! Definitely set up a second date!')
        else:
            print('Wooo! Successful date! Definitely set up a second date!')