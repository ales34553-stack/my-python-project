class student:

    class_year = 2025
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_students += 1


s1 = student("Alice", 20)
s2 = student("jaybobal", 22)
s3 = student("Charlie", 19)
s4 = student("David", 21)
s5 = student("Eve", 56)

#print(s1.name, s1.age)
#print(s2.name,s2.class_year)
#print(student.num_students)
print(f"my grauation year is {student.class_year} AND the number of students is {student.num_students}")
print("this is my student name)")
print(s1.name)
print(s2.name)
print(s3.name)
print(s4.name)
print(s5.name)