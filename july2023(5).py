class Student:
    def __init__(self, roll_number, name, age, grade):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.grade = grade

class SchoolAdministration:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_number, name, age, grade):
        if roll_number not in self.students:
            student = Student(roll_number, name, age, grade)
            self.students[roll_number] = student
            print(f"Student with roll number {roll_number} added successfully.")
        else:
            print(f"Student with roll number {roll_number} already exists.")

    def view_student(self, roll_number):
        if roll_number in self.students:
            student = self.students[roll_number]
            print(f"Roll Number: {student.roll_number}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
        else:
            print(f"Student with roll number {roll_number} not found.")


def main():
    school = SchoolAdministration()
    
    while True:
        print("\nSchool Administration Program")
        print("1. Add Student information")
        print("2. View Student information")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            school.add_student(roll_number, name, age, grade)
        elif choice == '2':
            roll_number = input("Enter Roll Number: ")
            school.view_student(roll_number)
        elif choice == '3':
            print("Exiting the School Administration Program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
