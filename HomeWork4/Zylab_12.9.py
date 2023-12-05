# Joshua Guajardo     PSID: 1811892


parts = input().split()  #input from the user into list
name = parts[0] # setting name from input list
while name != '-1':
    try:
        age = int(parts[1]) + 1 #converts age into integer and adding one
        print(f'{name} {age}') #printing name and age
    except ValueError:
        print(f"{name} 0") #error if wrong value is inputed



    parts = input().split()
    name = parts[0]




