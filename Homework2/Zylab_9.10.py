#Joshua Guajardo   PSID:1811892


import csv


file_name = input()

file_open = open(file_name)
word_file = csv.reader(file_open, delimiter=",")

list_word = []
for row in word_file:
    for word in row:
        list_word.append(word.strip())

for i in range(len(list_word)):
    if list_word[i] not in list_word[:i]:
        count = 0
        for w in list_word:
            if list_word[i] == w:
                count += 1
        print(list_word[i], count)
