#Auto Shop services
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

service_1 = input('Enter the first desired service: ')
service_2 = input('Enter the second desired service: ')

if service_1 == 'Oil change':
    print(f'{service_1} is of $35')
elif service_1 == 'Tire rotation':
    print(f'{service_1} is of $19')
elif service_1 == 'Car wash':
    print(f'{service_1} is of $7')
elif service_1 == 'Car wax':
    print(f'{service_1} is of $12')

if service_2 == 'Oil change':
    print(f'{service_2} is of $35')
elif service_2 == 'Tire rotation':
    print(f'{service_2} is of $19')
elif service_2 == 'Car wash':
    print(f'{service_2} is of $7')
elif service_2 == 'Car wax':
    print(f'{service_2} is of $12')
elif service_2 == '-':
    print('No Service')

print(f'{"Davy\'s auto shop services":^30}')
print(f'{"INVOICE":^30}')
print(f'{service_1}.......{dict[service_1]}')
print(f'{service_2}.......{dict[service_2]}')
total_amt = dict[service_1] + dict[service_2]
print(f'Total:{total_amt}')
