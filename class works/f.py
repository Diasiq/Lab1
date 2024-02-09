class Person:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname
    

class University():
    def __init__(self, name, faculties):
        self.name = name
        self.faculties = faculties

class Faculty():
    def __init__(self, courses, name):
        self.courses = courses
        self.name = name
          
SITE = Faculty("PP1", "PP2", "Discrete math", "Databases", name="SITE")
BS = Faculty("Startup", "Stocks", name="BS")
ISE = Faculty("Finance", "Microeconomic", "Macroeconomic", name="ISE")

KBTU = University("KBTU", ["SITE", "BS", "ISE"])

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname 



class Student(Person):
    def __init__(self, name, surname, ID, faculty, university):
        

        super().__init__(name, surname)
        self.ID = ID
        self.university = university
        self.faculty = self.university.faculties[faculty]
        self.courses = self.faculty.courses


    import random

class Student:
    def __init__(self, name, surname, ID, university, courses):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.university = university
        self.courses = courses

    def __str__(self):
        return self.name + " " + self.surname + " " + self.ID

    def passExam(self):
        mark = random.randint(0, 40)
        course = random.randint(0, len(self.courses) - 1)
        if mark >= 20:
            print(f"{self.name} has passed {self.courses[course]} with mark {mark}")
        else:
            print(f"{self.name} has not passed {self.courses[course]}. Mark is {mark}")

student = Student("Linus", "Torvalds", "22BD2024", "KBTU", ["SITE"])
student.passExam()


print(student.name)
print(student.surname)
print(student.ID)
print(student)