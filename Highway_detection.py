# highway detection machine
high_way = int(input('Enter a number: '))

if high_way >= 1 and high_way <= 99:
    print("It's a primary highway")
    if high_way % 2 == 0:
         print('Runs north/south')
    else:                           
         print('Runs east/west')        
elif high_way >= 100 and high_way <= 999:
     x = high_way % 100
     if x == 0:
          print('Invalid 00 not found')
     else:
          if x % 2 == 1:
               print("It's auxiliary highway")
               print('Runs north/south')
          else:
               print("It's auxiliary highway")
               print('Runs east/west')                          
else:
     print('Entered number is invalid')
