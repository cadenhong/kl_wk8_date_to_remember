# A Date To Remember - Using Python to Simulate a Date

## Simulating a date using two variables (one for user and one for date)

- Created a list called <b>Feelings</b> to rate the date: ['Uninterested', 'Maybe', 'Interested']

- Created a dictionary <b>Menu</b> to contain menu items: {'Salads': ['Chicken', 'Green', 'Quinoa'], 'Burgers': ['Classic', 'Veggie', 'Bean'], 'Sides': ['Fries', 'Wings', 'Coleslaw']}

- Created another dictionary <b>Price</b> to contain menu price based on same keys as Menu: {'Salads': 20, 'Burgers': 25, 'Sides': 15}

Ask user how much they have to calculate total price of menu items at the end. Allow user to select his/her own menu item and feelings about the date, but the date's selections will be generated randomly using the random module.

At the end, show how much the bill comes out to - if user does not have enough to pay, then have the date pay for remainder and this will impact the date's feelings about the dinner.

If either party is uninterested, outcome of this date will be that it was not a good match. If either party is a maybe and if either party chose a side as their menu, lean towards the date being not too promising. If either party is a maybe but they chose burger or salad, suggest going on another date. If both are interested, then this was a successful date!
