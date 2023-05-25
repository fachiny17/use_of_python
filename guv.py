from pract import Student

student1 = Student("Dare", 18, "Engineering", 3.5)
student2 = Student("Venessa", 17, "Nursing", 3.4)
student3 = Student("Louise", 23, "Financial Accounting", 2.4)

print("Dare's GPA is",student1.gpa)
print("Student's name is",student2.name)
print(student2.is_an_adult())
print(student1.is_intelligent())
