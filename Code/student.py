import os
class Student:
@staticmethod
def add_student():
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter student grade: ")
student = Student(name, age, grade)
student.save()
print("Student added successfully.")
@staticmethod
def update_student_details():
student_id = int(input("Enter the student ID to update details: "))
student = Student.get_student_by_id(student_id)
if student:
print(f"\nCurrent Details for Student ID {student_id}:")
print(student)
print("\nEnter new details:")
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter student grade: ")
student.update_details(name, age, grade)
print("Student details updated successfully.")
else:
print(f"No student found with ID {student_id}.")
@staticmethod
def remove_student():
student_id = int(input("Enter the student ID to remove: "))
student = Student.get_student_by_id(student_id)
if student:
Student.delete_student(student_id)
print(f"Student with ID {student_id} removed successfully.")
else:
print(f"No student found with ID {student_id}.")
def __init__(self, name, age, grade):
self.id = self.generate_id()
self.name = name
self.age = age
self.grade = grade
def __str__(self):
return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
def save(self):
with open("students.txt", "a") as file:
file.write(f"{self.id},{self.name},{self.age},{self.grade}\n")
@staticmethod
def get_all_students():
students = []
try:
with open("students.txt", "r") as file:
lines = file.readlines()
for line in lines:
data = line.strip().split(',')
student = Student(int(data[0]), data[1], int(data[2]), data[3])
students.append(student)
except FileNotFoundError:
pass
return students
@staticmethod
def get_student_by_id(student_id):
students = Student.get_all_students()
for student in students:
if student.id == student_id:
return student
return None
@staticmethod
def delete_student(student_id):
all_students = Student.get_all_students()
with open("students.txt", "w") as file:
for student in all_students:
if student.id != student_id:
file.write(f"{student.id},{student.name},{student.age},{student.grade}
\n")
def update_details(self, name, age, grade):
self.name = name
self.age = age
self.grade = grade
# Update the student information in the data file
all_students = Student.get_all_students()
with open("students.txt", "w") as file:
for student in all_students:
if student.id == self.id:
file.write(f"{self.id},{self.name},{self.age},{self.grade}\n")
else:
file.write(f"{student.id},{student.name},{student.age},{student.grade}
\n")
def generate_id(self):
if not os.path.exists("id_counter_students.txt"):
with open("id_counter_students.txt", "w") as counter_file:
counter_file.write("0")
with open("id_counter_students.txt", "r") as counter_file:
counter = int(counter_file.read())
counter += 1
with open("id_counter_students.txt", "w") as counter_file:
counter_file.write(str(counter))
return counter
