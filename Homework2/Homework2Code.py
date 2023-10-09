# Joshua Guajardo   PSID:1811892



import datetime

def date_pass(string_date):
    month_date = string_date.find(" ")
    day_date = string_date.find(",") + 2
    year_date = string_date.find(",") + 2

    if month_date != -1 and day_date != -1 and year_date != -1:
        month_new = string_date[:month_date]
        day_new = string_date[month_date + 1: day_date - 2]
        year_new = string_date[year_date:]
        return month_new, day_new, year_new
    else:
        month_new = 1
        day_new = 1
        year_new = 1
        return month_new, day_new, year_new


today = datetime.datetime.today()

int_file = "inputDates.txt"


with open(int_file, "r") as file:
    for line in file:
        str_date = line.strip()
        if str_date == '-1':
            break

while True:
    int_date = input()
    if int_date == '-1':
        break

    month_new, day_new, year_new = date_pass(int_date)

    if month_new == 1 or day_new == 1 or year_new == 1:
        continue
    else:
        date_new_format = datetime.datetime.strptime(f"{month_new} {day_new}, {year_new}", "%B %d, %Y")


    if date_new_format < today:
        date = date_new_format.strftime("%m/%d/%Y")
        print(date)


