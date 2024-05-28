#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     30/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime

currentDateTime = datetime.datetime.now()

class Person:
    def __init__(self, fName, lName, sex, gender, ssn, dob, email):
        self.fName = fName
        self.lName = lName
        self.sex = sex
        self.gender = gender
        self.ssn = ssn
        self.dob = dob
        self.email = email

    def printName(self):
        print(self.firstName, self.lastName)

class Faculty(Person):
    def __init__(self, fName, lName, sex, gender, ssn, dob, email, department, hireDate, hireYear):
        super().__init__(fName, lName, sex, gender, ssn, dob, email)
        self.department = department
        self.hireDate = hireDate
        self.hireYear = hireYear

    global faculty
    faculty = []



    def yearsOfService():
        global currentYear
        currentYear = 2019
        for x in faculty:
            serciveYears = currentYear - x.hireYear
            print(x.fName, x.lName, "has worked here for ", serciveYears, "years.")

class Student(Person):
    def __init__(self, fName, lName, sex, gender, ssn, dob, email, major, residenceHall, graduationYear, isEnrolled):
        super().__init__(fName, lName, sex, gender, ssn, dob, email)
        self.major = major
        self.residenceHall = residenceHall
        self.graduationYear = graduationYear
        self.isEnrolled = isEnrolled

    global students
    students = []

    def countStudents():
        global enrolledStudents
        enrolledStudents = 0
        for x in students:
            if x.isEnrolled == True:
                enrolledStudents += 1
        print("The numer of enrolled students is :", enrolledStudents)
