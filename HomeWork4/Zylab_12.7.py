# Joshua Guajardo   PSID: 1811892

def get_age(): # function used to get the users age
    age = int(input())
    if age <= 17 or age >= 75:
        raise ValueError('Invalid age.')
    return age


def fat_burning_heart_rate(age): # function to calculate heart rate
    heart_rate = (220 - age) * 0.7
    return heart_rate

if __name__ == "__main__": # main part of the code
    try:
        age = get_age()
        person_heart_rate = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {person_heart_rate:.1f} bpm')
    except ValueError as bad_input:
        print(bad_input)
        print('Could not calculate heart rate info.')
        print()