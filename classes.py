# keep it clean all the time as possible

# libraries
import random
from datetime import date
import datetime
# pip install pandas
# pip install openpyxl
import pandas as pd


class Admin:
    def __init__(self, identity, age, name, lastname, department, email, password, city, date):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.dep = department
        self.identity = identity
        self.email = email
        self.password = password
        self.city = city
        self.date = date

    def addStudent(self, identity, age, name, lastname, faculty, level):
        e_mail = name[0] + '.' + lastname + "@su.edu.eg"
        password = ''
        for i in range(7):
            value = random.randint(0, 9)
            password += str(value)
        newStudentData = [identity, age, name, lastname, faculty, level, e_mail, int(password)]
        studentData.loc[creatingStudents()] = newStudentData
        creatingStudentsNames()
        creatingStudents()
        print("Student added successfully :)")
        print(studentData)

    def updateStudent(self, email):
        check = email in list(studentData['email'])
        # view info
        if check == True:
            Index = list(studentData['email']).index(email)
            print(f'''
                    Student data:
                    1. ID: {students[Index].identity}
                    2. age: {students[Index].age}
                    3. first name: {students[Index].name}
                    4. last name: {students[Index].lastname}
                    5. faculty: {students[Index].faculty}
                    6. level: {students[Index].level}
                    7. email: {students[Index].email}
                    8. password: {students[Index].password}
                    ''')
            item = int(input("enter data number: "))
            if item == 1:
                newItem = int(input("enter new ID: "))
                studentData.loc[Index] = [newItem,
                                          students[Index].age,
                                          students[Index].name,
                                          students[Index].lastname,
                                          students[Index].faculty,
                                          students[Index].level,
                                          students[Index].email,
                                          students[Index].password]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            elif item == 2:
                newItem = int(input("enter new age: "))
                studentData.loc[Index] = [students[Index].identity,
                                          newItem,
                                          students[Index].name,
                                          students[Index].lastname,
                                          students[Index].faculty,
                                          students[Index].level,
                                          students[Index].email,
                                          students[Index].password]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            elif item == 3:
                newItem = input("enter new first name: ")
                studentData.loc[Index] = [students[Index].identity,
                                          students[Index].age,
                                          newItem,
                                          students[Index].lastname,
                                          students[Index].faculty,
                                          students[Index].level,
                                          students[Index].email,
                                          students[Index].password]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            elif item == 4:
                newItem = input("enter new last name: ")
                studentData.loc[Index] = [students[Index].identity,
                                          students[Index].age,
                                          students[Index].name,
                                          newItem,
                                          students[Index].faculty,
                                          students[Index].level,
                                          students[Index].email,
                                          students[Index].password]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            elif item == 5:
                newItem = input("enter new faculty: ")
                studentData.loc[Index] = [students[Index].identity,
                                          students[Index].age,
                                          students[Index].name,
                                          students[Index].lastname,
                                          newItem,
                                          students[Index].level,
                                          students[Index].email,
                                          students[Index].password]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            elif item == 6:
                newItem = int(input("enter new level: "))
                studentData.loc[Index] = [students[Index].identity,
                                          students[Index].age,
                                          students[Index].name,
                                          students[Index].lastname,
                                          students[Index].faculty,
                                          newItem,
                                          students[Index].email,
                                          students[Index].password]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            elif item == 7:
                newItem = input("enter new email: ")
                studentData.loc[Index] = [students[Index].identity,
                                          students[Index].age,
                                          students[Index].name,
                                          students[Index].lastname,
                                          students[Index].faculty,
                                          students[Index].level,
                                          newItem,
                                          students[Index].password]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            elif item == 8:
                newItem = int(input("enter new password: "))
                studentData.loc[Index] = [students[Index].identity,
                                          students[Index].age,
                                          students[Index].name,
                                          students[Index].lastname,
                                          students[Index].faculty,
                                          students[Index].level,
                                          students[Index].email,
                                          newItem]
                print("Student Data has beem successfully updated 👍️")
                print(studentData)
            else:
                print(f"there is no student data number {item} :(")

        else:
            print(f"{email} not found :(")

    def deleteStudent(self, email):
        check = email in list(studentData['email'])
        # view info
        if check == True:
            Index = list(studentData['email']).index(email)
            print("The following data will be deleted")
            print(f'''
                            Student data:
                            1. ID: {students[Index].identity}
                            2. age: {students[Index].age}
                            3. first name: {students[Index].name}
                            4. last name: {students[Index].lastname}
                            5. faculty: {students[Index].faculty}
                            6. level: {students[Index].level}
                            7. email: {students[Index].email}
                            8. password: {students[Index].password}
                            ''')
            print("are you sure?")
            print("1.yes\n2.no")
            sure = input("enter your choice: ")
            if sure.lower() in ['yes', "1", 'y', 'e', 's']:
                studentData.drop(labels= [Index+1], axis=0, inplace=True)
                print(studentData)
            else:
                print("Good choice :)")
            # delete
        else:
            print(f"{email} not found :(")


class Student:
    def __init__(self, identity, age, name, lastname, faculty, level, email, password):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.faculty = faculty
        self.level = level
        self.identity = identity
        self.email = email
        self.password = password

    def viewInfo(self, email):
        check = email in list(studentData['email'])
        if check == True:
            Index = list(studentData['email']).index(email)
            return f'''Your name is {students[Index].name} {students[Index].lastname}, 
            and your age is {students[Index].age}. You are in faculty of {students[Index].faculty} 
            in level {students[Index].level}. Id is {students[Index].identity}'''
        else:
            print(f"{email} not found :(")

    def viewSchedule(self, email):
        check = email in list(studentData['email'])
        today = datetime.date.today()
        if check == True:
            Index = list(studentData['email']).index(email)
            if 5 >= today.month >= 1:
                if (students[Index].faculty == 'it') and (students[Index].level == 1):
                    return '''
                    your schedule:
                    1. Electronics
                    2. intro to computer
                    3. ... 
                        '''
            elif 10 >= today.month >= 6:
                if students[Index].faculty.lower == 'it' and students[Index].level == 1:
                    return '''
                    your schedule:
                    1. programming one
                    2. logic gates
                    3. ... 
                        '''
        else:
            print(f"{email} not found :(")


# reading admin data
adminData = pd.read_excel('AdminData.xlsx', index_col=0)
print(adminData)
print("reading admin data done")

# reading student data
studentData = pd.read_excel('studentData.xlsx', index_col=0)
print(studentData)
print("reading student data done")

# creating admins
adminNames = []


def creatingAdminsNames():
    adminRows = adminData.iloc[0:].values
    for name in range(len(adminRows)):
        adminNames.append(adminRows[name][2])


creatingAdminsNames()
print(adminNames)
admins = []


def createAdmins():
    adminRows = adminData.iloc[0:].values
    for row in range(len(adminRows)):
        admin = Admin(adminRows[row][0], adminRows[row][1], adminRows[row][2], adminRows[row][3], adminRows[row][4],
                      adminRows[row][5], adminRows[row][6], adminRows[row][7], adminRows[row][8])
        admins.append(admin)


createAdmins()
print(admins)
print("creating admins done")
# test
print(admins[3].name)

# creating students
studentNames = []


def creatingStudentsNames():
    studentNames.clear()
    studentRows = studentData.iloc[0:].values
    for name in range(len(studentRows)):
        studentNames.append(studentRows[name][2])


creatingStudentsNames()
print(studentNames)
students = []


def creatingStudents():
    students.clear()
    studentRows = studentData.iloc[0:].values
    for row in range(len(studentRows)):
        student = Student(studentRows[row][0], studentRows[row][1], studentRows[row][2], studentRows[row][3],
                          studentRows[row][4], studentRows[row][5], studentRows[row][6], studentRows[row][7])
        students.append(student)
    return len(studentRows) + 1


creatingStudents()
print("creating students done")

