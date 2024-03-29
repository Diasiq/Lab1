class Person:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname
    
class Student(Person):
    def __init__(self, name, surname, ID):
        super().__init__(name, surname)
        self.ID = ID

    def __str__(self):
        return self.name + " " + self.surname + " " + self.ID
    
student = Student("Linus", "Torvalds", "22BD2024")

print(student.name)
print(student.surname)
print(student.ID)
print(student)


    