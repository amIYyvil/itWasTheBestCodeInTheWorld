# This program was written by Amy Anderson
# It is fully functional

# This program takes input from the user
# and generates that number of random integers.
# It then stores these values to a text file
# called randnums.txt

def main():
    import random
    
    try:
        outfile = open('randnums.txt','w')
        num_range = int(input('How many random numbers (in range '\
                          '1-500) would you like to generate? '))

        if num_range >= 1 and num_range <= 500:
            for count in range(1,num_range+1):
                number = random.randint(1,count)
                outfile.write(str(number)+'\n')
                
        else:
            print('Error! Number should be between 1 and 500.')
                   
                        
    except IOError as e:
        print('Something went wrong when '\
              'opening the file.')
        print(str(e))
    except ValueError:
        print('Error! Please enter a number between 1 and 500')
    except:
        print('An error has occurred!')
    finally:
        outfile.close()
        print()
        print('Success! '+ str(num_range)+' random numbers have been '+\
                      'recorded to the file randnums.txt.')    
main()
