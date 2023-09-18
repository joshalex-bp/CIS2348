# Joshua Guajardo    PISD:1811892

# Prompting user to enter the height and width of the wall
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))

# Calculating the wall area, paint needed for the wall, and a dictionary of paint prices
wall_area = int(wall_height * wall_width)
paint_amount = wall_area / 350
can_amount = round(paint_amount)
paintdict = {"red":35, "blue":25, "green":23}

# printing the wall area, paint needed and, cans needed for the wall
print('Wall area:', wall_area, 'square feet')
print('Paint needed: %.2f gallons' % paint_amount)
print('Cans needed:', can_amount, 'can(s)\n')

# Prompting the user to choose a color to paint the wall
paint_color = input('Choose a color to paint the wall:\n')

# Retrieving the price the user inputed from the dictionary
cost_gallon = paintdict[paint_color]

# Calculating the cost of the paint and printing out the cost
total_cost = cost_gallon * can_amount
print('Cost of purchasing', paint_color, 'paint: $%d' % total_cost)