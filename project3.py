#The dates for each season in the northern hemisphere are:
###Spring: March 20 - June 20     #march
###Summer: June 21 - September 21
###Autumn: September 22 - December 20
###Winter: December 21 - March 19

month = input('Enter a month: ')
date = int(input('Enter the date: '))

if date < 1 or date > 31:
    print('Entered date is invalid')
elif month == 'march':
    if date < 20:
        print('It\'s Spring')
    else:
        print('It\'s Winter')
elif month == 'april' or month == 'may':
    print('It\'s Spring')
elif month == 'june':
    if date < 20:
        print('It\'s Spring')
    else:
        print('It\'s Summer')
elif month == 'july' or month == 'august':
    print("It's Summer")
elif month == 'september':
    if date < 21:
        print("It's Summer")
    else:
        print("It's Autumn")
elif month == 'october' or month == 'november':
    print("It's Autumn")
elif month == 'december':
    if date < 20:
        print("It's Autumn")
    else:
        print("It's Winter")

elif month == 'january' or month == 'february':
        print("It's Winter")
else:
        print('Invalid entery')