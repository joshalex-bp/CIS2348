# Joshua Guajardo       PSID: 1811892

import csv
import datetime

class Records:         # class defined to create and manipulate objects
    def __init__(self, student_id, last_name, first_name, major, discipline):       #attributes used for students
        self.student_id = student_id           #assigns attribute to parameter
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.discipline = discipline
        self.gpa = None
        self.graduation_date = None

def read_data_file(file):        #function to read input files
    info = []
    with open(file, mode= 'r') as file:
        read_file = csv.reader(file)
        for row in read_file:
            info.append(row)
    return info

def process_student_info():     #function to process the three files
    student_info = read_data_file('StudentsMajorsList.csv')   #reads each file and makes them an object
    gpa_info = read_data_file('GPAList.csv')
    grad_info = read_data_file('GraduationDatesList.csv')

    student_dict = {}

    for data in student_info: #for loop used to iterate over the students major list and uses their student id as a key to assign them in the dictionary
        student_id, last_name, first_name, major, discipline = data  #unpacks the values of data and used for indexing
        student_data = Records(student_id, last_name, first_name, major, discipline) #calls the records class and passes the attributes as class objects
        student_dict[student_id] = student_data      #puts the values into the dictionary and uses the student id as a key

    for data in gpa_info: #for loop that extracts the gpa info object into the student dictionary
        student_id, gpa = data
        student_dict[student_id].gpa = float(gpa)  #converts string to float

    for data in grad_info:  #for loop that extracts graduation dates into the student dictionary
        student_id, grad_date = data
        student_dict[student_id].graduation_date = datetime.datetime.strptime(grad_date, "%m/%d/%Y") # datetime used to see if student has graduated or not


    sort_students = sorted(student_dict.values(), key=sort_last_name)     #creates a new object that sorts the student dictionary by last names

    return sort_students



def sort_last_name(student): #funtion used to sort by last names
    return student.last_name

def sort_gpa(student): #function used to sort by gpa
    return student.gpa

def sort_grad_date(student): #function used to sort by graduation date
    return student.graduation_date


def student_query(sort_students): #function for query
    while True:
        try:
            q_major = input('Enter major \n')  #sets input as object
            q_gpa = float(input('Enter GPA \n')) #sets input as object
        except ValueError:
            print('Invalid Input.' #what is oupttued when an value error has occured
            continue

        filter_student = [] #list for the students who meet the major query
        for kid in sort_students:
            if q_major.lower() == kid.major.lower():  #checking to see if a students' major matches the query and appends the student to the list
                filter_student.append(kid)


        range_students = [] #list for the gpa of students
        for kid in sort_students:
            if abs(q_gpa - kid.gpa) <= 0.1: #checks to see if the gpa maches the query and appends them to the list
                range_students.append(kid)

        print('Your student(s):')  #outputs the mached students information
        if range_students:
            for kid in range_students:
                print(f'{kid.student_id}: {kid.first_name} {kid.last_name}, GPA: {kid.gpa}')

            today_date = datetime.datetime.now() #sets todays date as an object

            consider_kids = [] #creates list for students to consider



            for kid in filter_student:     ##checks to see if students in list are near the querys inputs
                if 0.1 < abs(q_gpa - kid.gpa) <= 0.25 and kid.graduation_date > today_date:
                    consider_kids.append(kid)
                    print('\n You may also consider:') #outputs the stuidents who are near the querys inputs
                    print(f'{kid.student_id}: {kid.first_name} {kid.last_name}, GPA: {kid.gpa}')
            if not consider_kids:
                print('There are no other students to recommend') #outputs when no match is found

        else:
            second_closest = min(filter_student, key=sort_gpa) #finding the student with the minimum GPA
            if second_closest: #if the list is not empty print the students information
                print('No students withhin the range. Closest range is: ')
                print(f'{second_closest.student_id}: {second_closest.first_name} {second_closest.last_name} GPA:{second_closest.gpa}')

        user_input = input("Enter 'q' to quit or press Enter to continue \n") #prompts the user to quit or keep going
        if user_input == 'q':
            break

if __name__ == "__main__": #main section of the code

    gather_data = process_student_info() #function to read and sort files

    student_query(gather_data) #handles the querys'




