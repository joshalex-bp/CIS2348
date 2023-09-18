# Joshua Guajardo    PISD:1811892

# Prompting the user to enter the amounts of ingredients
lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

# Printing the users input and converting them to float numbers with two decimal points
print('\nLemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar))

# Prompting the user to enter desired amount of servings
servings_2 = float(input('\nHow many servings would you like to make?\n'))


# Printing how many cups needed to make the servings
print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_2))
print('{:.2f} cup(s) lemon juice'.format(lemon * servings_2 / servings))
print('{:.2f} cup(s) water'.format(water * servings_2 / servings))
print('{:.2f} cup(s) agave nectar\n'.format(agave_nectar * servings_2 / servings))

# Converting the cups needed from the previous output into gallons and printing them out
print('Lemonade ingredients - yields {:.2f} servings'.format(servings_2))
print('{:.2f} gallon(s) lemon juice'.format(lemon * servings_2 / servings / 16))
print('{:.2f} gallon(s) water'.format(water * servings_2 / servings / 16))
print('{:.2f} gallon(s) agave nectar'.format(agave_nectar * servings_2 / servings / 16))