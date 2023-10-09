#Joshua Guajardo   PSID:1811892


def exact_change(total):
    dollar_value = 100
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    penny_value = 1

    num_dollars = total // dollar_value
    total %= dollar_value

    num_quarters = total // quarter_value
    total %= quarter_value

    num_dimes = total // dime_value
    total %= dime_value

    num_nickels = total // nickel_value
    total %= nickel_value

    num_pennies = total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    in_total = int(input())


num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(*in_total)

if in_total <= 0:
    print('no change')
else:
    if num_dollars == 1:
        print('1 dollar')
    elif num_dollars > 1:
        print(num_dollars, 'dollars')

    if num_quarters == 1:
        print('1 quarter')
    elif num_quarters > 1:
        print(num_quarters, 'quarters')

    if num_dimes == 1:
        print('1 dime')
    elif num_dimes > 1:
        print(num_dimes, 'dimes')

    if num_nickels == 1:
        print('1 nickel')
    elif num_nickels > 1:
        print(num_nickels, 'nickels')

    if num_pennies == 1:
        print('1 penny')
    elif num_pennies > 1:
        print(num_pennies, 'pennies')






