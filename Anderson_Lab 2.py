#"Cookie Recipe Translator", by Amy Anderson
#
#This program is complete and functioning
#"Cookie Recipe Translator" allows its user
#to calculate the precise amount of
#ingredients needed to make any
#number of cookies they desire.

#Design a constant amount of each ingredient
#needed to make one cookie
cups_butter = 1.5/48
cups_sugar = 1.0/48
cups_flour = 2.75/48

#Ask the user how many cookies they will be making
num_cookies = int(input('How many cookies would you like to make? '))

#Conveniently deliver a precise amount of each
#ingredient needed to make the user's amount
#of cookies

print('To make',num_cookies,'cookies, you will need:')

print(format(num_cookies*cups_butter,'.2f'),'cups of butter')

print(format(num_cookies*cups_sugar,'.2f'),'cups of sugar')

print(format(num_cookies*cups_flour,'.2f'),'cups of flour')
      
