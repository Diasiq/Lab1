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
    def __init__(self, *courses, name):
        self.courses = list(courses)
        self.name = name
          
SITE = Faculty("PP1", "PP2", "Discrete Math", "Databases", name="SITE")
BS = Faculty("Startup", "Stocks", name="BS")
ISE = Faculty("Finance", "Microeconomic", name="ISE")

KBTU = University("KBTU", [SITE, BS, ISE])

class Student(Person):
    def __init__(self, name, surname, ID, university, faculty_index):
        super().__init__(name, surname)
        self.ID = ID
        self.university = university
        self.faculty = self.university.faculties[faculty_index]
        self.courses = self.faculty.courses

    def __str__(self):
        return super().__str__() + " " + self.ID
   
    
student = Student("Linus", "Torvalds", "22BD2024", KBTU, 0)

print(student.name)
print(student.surname)
print(student.ID)
print(student)
