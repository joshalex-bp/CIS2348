# Joshua Guajardo    PSID:1811892

def stronger_password(password):
    new_letter = {"i": "!", "a" : "@", "m" : "M" , "B" : "8", "o" : "."}
    newpassword = ""

    for letter in password:
        if letter in new_letter:
            newpassword += new_letter[letter]
        else:
            newpassword += letter

    newpassword += "q*s"
    return newpassword

password = input()

better_pw = stronger_password(password)

print(better_pw)