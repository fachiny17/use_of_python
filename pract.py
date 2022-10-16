class Student:
    def __init__(self, name, age, subject, gpa):
        self.name = name
        self.age = age
        self.subject = subject
        self.gpa = gpa
    
    def is_an_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    def is_intelligent(self):
        if self.gpa >= 3.0:
            return True
        else:
            return False