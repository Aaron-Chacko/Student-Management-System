from student import Student
from fees import Fees
def home_page():
print("\nStudent and Fees Management System")
print("1. Student Details")
print("2. Fees Details")
print("3. Quit")
if __name__ == "__main__":
while True:
home_page()
choice = input("Enter your choice (1/2/3): ")
if choice == "1":
while True:
print("\nStudent Details Menu")
print("1. Add Student")
print("2. Update Student Details")
print("3. Remove Student")
print("4. View Students with Pending Fees")
print("5. Back to Home Page")
student_choice = input("Enter your choice (1/2/3/4/5): ")
if student_choice == "1":
Student.add_student()
elif student_choice == "2":
Student.update_student_details()
elif student_choice == "3":
Student.remove_student()
elif student_choice == "4":
Fees.display_students_with_pending_fees()
elif student_choice == "5":
break
else:
print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
elif choice == "2":
while True:
print("\nFees Details Menu")
print("1. Add Fees Payment")
print("2. View Students with Pending Fees")
print("3. Back to Home Page")
fees_choice = input("Enter your choice (1/2/3): ")
if fees_choice == "1":
Fees.add_fees_payment()
elif fees_choice == "2":
Fees.display_students_with_pending_fees()
elif fees_choice == "3":
break
else:
print("Invalid choice. Please enter 1, 2, or 3.")
elif choice == "3":
print("Exiting the program. Goodbye!")
break
else:
print("Invalid choice. Please enter 1, 2, or 3.")
