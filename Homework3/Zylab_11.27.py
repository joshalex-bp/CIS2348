#Joshua Guajardo     PSID:1811892

roster_dic = {}

for i in range(1, 6):
    jersey_number = int(input("Enter player {}'s jersey number:\n".format(i)))
    rating_number = int(input("Enter player {}'s rating:\n".format(i)))
    roster_dic[jersey_number] = rating_number
    print()

print("ROSTER")
for key in sorted(roster_dic.keys()):
    print("Jersey number: {}, Rating: {}".format(key, roster_dic[key]))
print()


trill = True
while trill == True:
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    print('Choose an option:')

    user_choice = input()
    if user_choice == 'o':
        print("ROSTER")
        for key in sorted(roster_dic.keys()):
            print("Jersey number: {}, Rating: {}".format(key, roster_dic[key]))
        print()

    elif user_choice == 'a':
        print("Enter a new player's jersey number: ")
        jersey_number = int(input())
        print("Enter the player's rating: ")
        rating_number = int(input())
        roster_dic[jersey_number] = rating_number
    elif user_choice == 'd':
        print('Enter a jersey number: ')
        jersey_number = int(input())
        if jersey_number in roster_dic:
            del roster_dic[jersey_number]
    elif user_choice == 'u':
        print("Enter a new player's jersey number: ")
        jersey_number = int(input())
        print("Enter the player's rating: ")
        new_rating_number = int(input())
        roster_dic[jersey_number] = new_rating_number
    elif user_choice == 'r':
        print('Enter a rating: ')
        rating_num = int(input())
        print('ABOVE {}'.format(rating_num))
        for j, r in roster_dic.items():
            if r > rating_num:
                print("Jersey number {}, Rating: {}".format(j, r))
    elif user_choice == 'q':
        trill = False
