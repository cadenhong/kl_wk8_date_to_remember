# A Date To Remember - Using Python to Simulate a Date

<p align="center">
  <img src="https://media.istockphoto.com/vectors/people-at-a-table-talking-icon-isolated-on-white-background-vector-vector-id1076598642?k=20&m=1076598642&s=612x612&w=0&h=yKryl2p8ViW7owm5fyjVEHS40PTa1o31j2UhvDQ--NU=" alt="date" width="250"/>
</p>

### Description
Simulate a date by running [Activity_aDateToRemember.py](https://github.com/cadenhong/kl_wk8_date_to_remember/blob/main/Activity_aDateToRemember.py).

Ask user how much money they have to pay the total price of menu items at the end. Allow user to select his/her own menu item and feelings about the date, but the date's selections will be generated randomly using the `random` module.

At the end, show how much the bill comes out to - if user does not have enough to pay, then have the date pay for remainder and this will impact the date's feelings about the dinner.

#### Variables Used
- `user` and `date` - user's decisions are all input based and date's decisions are all randomly generated
- Created a list called <b>Feelings</b> to rate the date: `['Uninterested', 'Maybe', 'Interested']`
- Created a dictionary <b>Menu</b> to contain menu items: `{'Salads': ['Chicken', 'Green', 'Quinoa'], 'Burgers': ['Classic', 'Veggie', 'Bean'], 'Sides': ['Fries', 'Wings', 'Coleslaw']}`
- Created another dictionary <b>Price</b> to contain menu price based on same keys as Menu: `{'Salads': 20, 'Burgers': 25, 'Sides': 15}`

#### Results
- If either party is uninterested, outcome of this date will be that it was not a good match
- If either party is a maybe and if either party chose a side as their menu, lean towards the date being not too promising
- If either party is a maybe but they chose burger or salad, suggest going on another date
- If both are interested, then this was a successful date!
