# Joshua Guajardo PISD 1811892

# Displays Birthday Calculator and current day
print('Birthday Calculator')
print('Current Day')

# Prompting the user to entering the current day converting them into integer values
month_now = int(input('Month:'))
day_now = int(input('Day:'))
year_now = int(input('Year:'))

print('Birthday')

# Prompting the user to enter thier birthday converting it into integer values
bd_month = int(input('Month:'))
bd_day = int(input('Day:'))
bd_year = int(input('Year:'))

# calulating how old the user is by subtracting the current year by the year the user was born
year_calculate = year_now - bd_year

# A branch used to determine if it is the users birthday and if not prints how old they are 
if month_now == bd_month and day_now == bd_day:
    print('Happy Birthday!')
else:
    print('You are', year_calculate, 'years old.')