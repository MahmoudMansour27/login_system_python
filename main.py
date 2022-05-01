# keep it clean all the time as possible

# libraries
from classes import *


def log_Student():
    print(" ")
    print("Student login")
    print(" ")
    username = input("Enter email:")
    password = input("Enter Password:")
    if username in list(studentData['email']):
        print("right email")
        Index = list(studentData['email']).index(username)
        print(Index)
        print(type(list(studentData['password'])[Index]))
        if int(password) == int(list(studentData['password'])[Index]):
            while 1:
                print('''
                1.View Info
                2.View Schedule
                3. Back
                ''')
                choice = int(input("Enter: "))
                if choice == 1:
                    Index = list(studentData['email']).index(username)
                    print(students[Index].viewInfo(username))
                elif choice == 2:
                    Index = list(studentData['email']).index(username)
                    print(students[Index].viewSchedule(username))
                elif choice == 3:
                    break
                else:
                    print("invalid!")
        else:
            print("incorrect password :(")
    else:
        print("invalid! Please enter email and password again.")


def admin_session():
    print("Login Success")


def log_Admin():
    print(" ")
    print("Admin login")
    print(" ")
    username = input("Enter email:")
    password = input("Enter Password:")
    if username in list(adminData['email']):
        print("right email")
        Index = list(adminData['email']).index(username)
        print(Index)
        print(type(list(adminData['password'])[Index]))
        if int(password) == int(list(adminData['password'])[Index]):
            while 1:
                print('''
                            1. Add Student
                            2. Update Student
                            3. Delete Student
                            4. Back
                            ''')
                choice = int(input("Enter: "))
                if choice == 1:
                    Index = list(adminData['email']).index(username)
                    identity = int(input("Enter ID number:"))
                    age = int(input("Enter age:"))
                    name = input("Enter first name:")
                    lastname = input("Enter last name:")
                    faculty = input("Enter faculty name:")
                    level = int(input("Enter level:"))
                    admins[Index].addStudent(identity, age, name, lastname, faculty, level)
                elif choice == 2:
                    Index = list(adminData['email']).index(username)
                    studentEmail = input("Enter Student email:")
                    admins[Index].updateStudent(studentEmail)
                elif choice == 3:
                    Index = list(adminData['email']).index(username)
                    studentEmail = input("Enter Student email:")
                    admins[Index].deleteStudent(studentEmail)
                elif choice == 4:
                    break
                else:
                    print("invalid!")
        else:
            print("incorrect password :(")
    else:
        print("invalid! Please enter user name and password again.")


def main():
    while 1:
        print("Welcome to the Faculty System")
        print(" ")
        print("1.Admin")
        print("2.Student")
        print("3.Exit")

        user_option = input("Option : ")
        if user_option in ["1", "one", "admin", "Admin"]:
            log_Admin()
        elif user_option in ["2", "two", "student", "Student"]:
            log_Student()
        elif user_option in ["3", "three", "exit", "Exit"]:
            print("Exit")
            break
        else:
            print("No valid option was selected")


main()



