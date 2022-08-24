# A Date to Remember!

import random

def separator():
    print("------------------------------------------------------------")

user = "Caden"
date = "Casey"
restaurant = "Kura Diner"
feelings = ['Uninterested', 'Maybe', 'Interested']
menu = {'Salads': ['Chicken', 'Green', 'Quinoa'], 'Burgers': ['Classic', 'Veggie', 'Bean'], 'Sides': ['Fries', 'Wings', 'Coleslaw']}
price = {'Salad': 20, 'Burger': 25, 'Sides': 15}

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
                userItem = input(f'\nChoose an item from {menu[userCategory]}: ')
                if userItem.capitalize() in menu[userCategory]:
                    userItem = userItem.capitalize()
                    break
                else:
                    print("Invalid category!")
            break
        else:
            print(f'Invalid category! Select from {menu.keys()}!')

    dateCategory = random.choice(list(menu.keys()))
    dateRandom = random.randint(0,2)
    dateItem = menu[dateCategory][dateRandom]

    userFeeling = input(f'\nAn order of {userItem} - {userCategory} for {user}, and {dateItem} - {dateCategory} for {date}!\n\n**Whisper**\nSo {user}, how is the date going so far? Choose from {feelings}: ')
    
    userFeeling = userFeeling.capitalize()
    dateFeeling = random.choice(feelings)

    separator()

    total = price[userCategory] + price[dateCategory]
    money = money - total

    print(f'Hope you enjoyed your meals. Your total bill comes out to ${total}')
    
    if money < 0:
        print(f'\nYour card got declined - there\'s not enough money, the balance is ${money}')
        print(f'{date} - please cover the rest!')
        if dateFeeling == 'Interested':
            print(f'{date} mentioned that they were {dateFeeling}, but unfortunately, that is not the case anymore...')
            dateFeeling = 'Uninterested'
        print(f'{user}, sorry to break it to you but seems like {date} is not interested in a second date... Good luck!')
    else:
        print(f'\nThanks for the payment, {user}! You now have ${money} left')

        if userFeeling == 'Uninterested' or dateFeeling == 'Uninterested':
                print(f'Both of you agreed that this wasn\'t a good match - there won\'t be another date!')
        elif userFeeling == 'Maybe' or dateFeeling == 'Maybe':
            if userCategory == 'Sides' or dateCategory == 'Sides':
                print("Hmm... Picking a side on a date does not seem too promising... You guys should talk it out and decide on next steps...")
            else:
                print("Forget about feeling unsure! You guys make a good couple, go on another date!")
        else:
            print('Wooo! Successful date! Definitely set up a second date!')