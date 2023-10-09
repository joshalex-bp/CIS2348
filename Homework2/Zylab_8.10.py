# Joshua Guajardo    PSID:1811892

def palindrome_dome(word):

    word_nospace = word.replace(" ", "")

    word_rev = word_nospace[::-1]



    if word_nospace == word_rev:
        print(word, 'is a palindrome')
    else:
        print(word, 'is not a palindrome')

in_word = input()

palindrome_dome(in_word)