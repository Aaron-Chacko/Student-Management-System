from student import Student
class Fees:
@staticmethod
def add_fees_payment():
student_id = int(input("Enter the student ID: "))
student = Student.get_student_by_id(student_id)
if student:
fees_payment = float(input("Enter fees payment amount: "))
student.fees -= fees_payment
print(f"Fees payment of {fees_payment} recorded for {student.name}.")
student.update_details(student.name, student.age, student.grade) # Update
student details
else:
print(f"No student found with ID {student_id}.")
@staticmethod
def display_students_with_pending_fees():
students = Student.get_all_students()
print("\nStudents with Pending Fees:")
print("---------------------------")
for student in students:
if student.fees > 0:
print(f"{student.name} (ID: {student.id}) - Pending Fees: {student.fees}")
