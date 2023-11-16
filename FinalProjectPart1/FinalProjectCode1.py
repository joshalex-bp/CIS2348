# Joshua Guajardo     PSID:1811892

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

    student_dict = {}  #an empty dictionary to store all student information


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


def sort_last_name(name): #funtion used to sort by last names
    return name.last_name

def sort_gpa(smart_kid): #function used to sort by gpa
    return smart_kid[4]

def sort_grad_date(date): #function used to sort by graduation date
    return date[3]


def write_roster_file(sort_students):    #function used to write the full roster file

    full_roster = []     #list to store information

    for student in sort_students:       #for loop that iterates over the sorted list
        row = [student.student_id, student.major, student.first_name, student.last_name, student.gpa, student.graduation_date.strftime("%m/%d/%Y"), student.discipline]   # grabs attributes from the list

        full_roster.append(row)  #adds them to the roster list

    with open('FullRoster.csv', mode='w', newline='') as file:    #writes the roster list into a csv file
        write_file = csv.writer(file)
        write_file.writerows(full_roster)


def write_major_file(sort_students): #function used to to write major files

    major = {} #dictionary used to store major information

    for student in sort_students: #for loop that iterates over sorted list
        major_info = f"{student.major.replace(' ', '')}Students.csv"   #creates a string for each major and removes the spaces between each word
        if major_info not in major: #if a major is not in the dictionary  it creates a new new list
            major[major_info] = []
        major[major_info].append([student.student_id, student.last_name, student.first_name, student.graduation_date.strftime("%m/%d/%Y"), student.discipline]) #appends the attributes to each major list


    for major_info, major in major.items(): # for loop to write a file for each major and the information
        with open(major_info, mode='w', newline='') as file:
            write_file = csv.writer(file)
            write_file.writerows(major)



def write_scholarship_students(sort_students): #function to write scholarship students

    scholarship_students = [] #list created to store students

    today_date = datetime.datetime.now().date() #used to establish today's date

    for student in sort_students:  # if function used to see if student qualifies for scholarship and if they are append them to the list
        if student.gpa > 3.8 and student.graduation_date.date() >= today_date and student.discipline != 'Y':
            scholarship_students.append([student.student_id, student.last_name, student.first_name, student.major, student.gpa])

    scholarship_students.sort(key=sort_gpa, reverse=True) #used to sort the list by gpa

    with open('ScholarshipCandidates.csv', mode='w', newline='') as file: #writes a file with all the scholarship students
        write_file = csv.writer(file)
        write_file.writerows(scholarship_students)


def write_discipline_students(sort_students): #function used to write bad kids list

    discipline_students = [] # list to store discipline students

    for student in sort_students: # for loop to see if student is a bad and if they are append their attributes to the list
        if student.discipline == 'Y':
            discipline_students.append([student.student_id, student.last_name, student.first_name, student.graduation_date.strftime("%m/%d/%Y")])

    discipline_students.sort(key=sort_grad_date, reverse=True) #used to sort the students by graduation dates

    with open('DisciplinesStudents.csv', mode='w', newline='') as file: #writes discipline list to new file
        write_file = csv.writer(file)
        write_file.writerows(discipline_students)



if __name__ == "__main__":  #main part of the code used to execute all the functions to get the files
    sort_students = process_student_info()

    write_major_file(sort_students)
    write_roster_file(sort_students)
    write_discipline_students(sort_students)
    write_scholarship_students(sort_students)