# Joshua Guajardo    PISD:1811892

# Prints out the services of davy's shop with proces
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

# Prompting the user to select two services
first_service = input('Select first service:\n')
second_service = input('Select second service:\n')

# A dictionary for the services with their prices
shop_dic = {"Oil change":35, "Tire rotation":19, "Car wash":7, "Car wax":12}
total_service = 0

# Priting an invoice of the users choices along with the total price
print("\nDavy's auto shop invoice\n")

# An if branch that retrieves the price of the service and totaling the price
if first_service in shop_dic:
    print('Service 1: {0}, ${1}'.format(first_service,shop_dic[first_service]))
    total_service += shop_dic[first_service]

if first_service == '-':
    print('Service 1: No service')

if second_service in shop_dic:
    print('Service 2: {0}, ${1}\n'.format(second_service,shop_dic[second_service]))
    total_service += shop_dic[second_service]
if second_service == '-':
    print('Service 2: No service\n')
print('Total: ${0}'.format(total_service))