# A Date to Remember!

import random

def separator():
    print("----------------------------------------------------------------------")

user = "Caden"
date = "Casey"
restaurant = "Kura Diner"
feelings = ['Uninterested', 'Maybe', 'Interested']
menu = {'Salads': ['Chicken', 'Green', 'Quinoa'], 'Burgers': ['Classic', 'Veggie', 'Bean'], 'Sides': ['Fries', 'Wings', 'Coleslaw']}
price = {'Salads': 20, 'Burgers': 25, 'Sides': 15}

separator()
print(f'A Date To Remember at {restaurant}'.center(70))
separator()
print(f'Hi {user} and {date}! Welcome to {restaurant}!\nHope you lovebirds have a great time!\n')
money = int(input("Enter how much money you brought for tonight: $"))

if money < 30:
    separator()
    print('Sorry, the minimum is $30 - you don\'t have enough to dine here tonight')
    separator()
else:
    separator()
    print(f'{restaurant}\'s Menu\n'.center(70))
    for item in menu:
        print(f'{item}, ${price[item]}'.center(70))
    separator()

    while True:
        userCategory = input("\nWhich category would you like to choose from? ")
        checkUserInput = menu.get(userCategory.capitalize())
        if checkUserInput is not None:
            while True:
                userCategory = userCategory.capitalize()
                print(f'From {userCategory} category, select one:', ', '.join(menu[userCategory]))
                userItem = input('\nWhich item would you like? ')
                if userItem.capitalize() in menu[userCategory]:
                    userItem = userItem.capitalize()
                    break
                else:
                    print(f'\nInvalid menu item!')
            break
        else:
            print(f'Invalid category! Select from', ', '.join(menu))

    dateCategory = random.choice(list(menu.keys()))
    dateRandom = random.randint(0,2)
    dateItem = menu[dateCategory][dateRandom]

    separator()
    print("YOUR ORDER".center(70))
    print(f'{user}: {userItem} ({userCategory})'.center(70))
    print(f'{date}: {dateItem} ({dateCategory})'.center(70))
    separator()
    
    print(f'**Whisper**'.center(70))
    print(f'So {user}...'.center(70))
    while True:
        userFeeling = input(f'\nHow is the date going so far? Choose from {feelings}: ')
        if userFeeling.capitalize() not in feelings:
            print("Invalid input!")
        else:
            userFeeling = userFeeling.capitalize()
            dateFeeling = random.choice(feelings)
            break

    separator()

    total = price[userCategory] + price[dateCategory]
    money = money - total

    print(f'Hope you enjoyed your meals. Your total bill comes out to ${total}')
    
    if money < 0:
        print(f'\nYour card got declined - there\'s not enough money, the balance is ${money}')
        print(f'{date} - please cover the rest!')
        if dateFeeling == 'Interested':
            print(f'\n{date} mentioned that they were {dateFeeling}, but unfortunately, that is not the case anymore...')
            dateFeeling = 'Uninterested'
        print(f'{user}, sorry to break it to you but seems like {date} is not interested in a second date... Good luck!')
        separator()
    else:
        print(f'\nThanks for the payment, {user}! You now have ${money} left')
        separator()

        print(f'{user}\'s feeling: {userFeeling}\n{date}\'s feeling: {dateFeeling}\n' )

        if userFeeling == 'Uninterested' or dateFeeling == 'Uninterested':
                print(f'Both of you agreed that this wasn\'t a good match - there won\'t be another date!')
        elif userFeeling == 'Maybe' or dateFeeling == 'Maybe':
            if userCategory == 'Sides' or dateCategory == 'Sides':
                print("Hmm... Picking a side on a date doesn't seem too promising but talk it out and decide on next steps.")
            else:
                print("Forget about feeling unsure! No one went with a side and from what I saw, you guys make a good couple. Go on another date!")
        else:
            print('Wooo! Who cares about what you ate! You\'re both interested so it\'s a successful date! Definitely set up a second date!')

separator()