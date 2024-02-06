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
          
SITE = Faculty("PP1", "PP2", "Discrete math", "Databases")
BS = Faculty("Startup", "Stocks")
ISE = Faculty("Finance", "Microeconomic", "Macroeconomic")

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


    def __str__(self):
        return self.name + " " + self.surname + " " + self.ID
   
    
student = Student("Linus", "Torvalds", "22BD2024", "KBTU", "SITE")

print(student.name)
print(student.surname)
print(student.ID)
print(student)