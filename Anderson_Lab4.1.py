# Written by Amy Anderson
# This program is complete
# This program collects a
# user's budget and spending
# and displays budget, total
# spent, and whether the user
# spent within their budget.

budget = float(input('How much would you like to \
spend this month?(Press 0 for total): $'))
total = 0
price = float(input('Enter the price: $'))
total += price

while price != 0:
    price = float(input('Enter the price(press 0 for total): $'))
    total += price
    over_budget = total - budget
    under_budget = budget - total

    

if total < budget:
    print('Budgeted: $',\
          format(budget,',.2f'),sep='')
    print('Spent: $',\
          format(total,',.2f'),sep='')
    print('Congrats! You are $',\
          format(under_budget,',.2f'),sep='',end=' ')
    print('under budget!')

elif total > budget:
    print('Budgeted: $',\
          format(budget,',.2f'),sep='')
    print('Spent: $',\
          format(total,',.2f'),sep='')
    print('Uh-Oh! You are $',\
          format(over_budget,',.2f'),sep='',end = ' ')
    print('Over budget! Try using a different '\
          'strategy next month!')
    
