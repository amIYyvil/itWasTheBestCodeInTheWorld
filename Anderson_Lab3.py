# This program calculates a user's discounted
# amount and total amount due depending on how
# many packages were purchased.

# First, collect the amount of packages
# from the user

quantity = int(input('Enter the number of packages purchased: '))

if quantity >= 100:
    discount = 0.4      
    price = 99*quantity                # This line creates a subtotal
    totalDue = price-(price*discount)  # Price after discount
    print ('Discount amount:$',\
           format(price*discount, '.2f'),
           sep='')                     # Amount $ saved
    print ('Total Due:$',\
           format(totalDue, '.2f'),    
           sep='')                     # Finally, the total.

elif quantity >=50 and quantity <=99:
    discount = 0.3
    price = 99*quantity
    totalDue = price-(price*discount)
    print ('Discount Amount:$',\
           format(price*discount, '.2f'),
           sep='')
    print('Total Due:$',\
          format(totalDue, '.2f'),
          sep='')

elif quantity >=20 and quantity <=49:
    discount = 0.2
    price = 99*quantity
    totalDue = price-(price*discount)
    print ('Discount Amount:$',\
           format(price*discount, '.2f'),
           sep='')
    print ('Total Due:$',\
           format(totalDue, '.2f'),
           sep='')
           
elif quantity >=10 and quantity <=19:
    discount = 0.1
    price = 99*quantity
    totalDue = price-(price*discount)
    print ('Discount Amount:$',\
           format(price*discount, '.2f'),
           sep='')
    print ('Total Due:$',\
           format(totalDue, '.2f'),
           sep='')

else:                                  #No discount for penny pinchers
    discount = 0
    price = 99*quantity
    totalDue = price-(price*discount)
    print ('Discount Amount:$',\
           format(price*discount, '.2f'),
           sep='')
    print ('Total Due:$',\
           format(totalDue, '.2f'),
           sep='')
