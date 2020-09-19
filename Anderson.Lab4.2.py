# Written by Amy Anderson
# This program is complete
# This program calculates
# the amount the ocean
# will have risen over the
# next 25 years.

RISE = 1.8

print('Year', '\t','Rise (in millimeters')
print('---------------------------------')


for year in range (1,26):
    amount_risen = year * RISE
          
    print (format(year,'.0f'),'\t',format(amount_risen,'.2f'))
