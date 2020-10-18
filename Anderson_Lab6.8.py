# This program was written by Amy Anderson
# It is fully functional

# Lab 6.8 opens, reads, and displays
# the properties of the random numbers
# recorded in the randnums.txt file.
# 

def main():
    number = 0
    total = 0
    try:
        infile = open('randnums.txt','r')

        for line in infile:
            total += float(line)
            number += 1

        print('The sum of your numbers '\
              'is ' + str(total))
        print()
        print('There are '+ str(number)+\
              ' numbers in this file.')
        print()
        print('The average of the numbers '+\
              'is: ' + str(format(total/number,'.2f')))
        
        

    except IOError as e:
        print('ERROR! Cannot access file.')
        print(str(e))
    except ValueError as v:
        print('ERROR! Invalid value.')
        print(str(v))
    except Exception as E:
        print('An error has occurred')
        print(E)
    finally:
        infile.close()
main()
