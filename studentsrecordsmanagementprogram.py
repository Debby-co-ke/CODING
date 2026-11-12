#Using List data structure to manage student records
students_records = []

def add_student(): # Function to add a student record
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    student  = (student_id, name, course)
    students_records.append(student)

    print("Student added successfully!")

def view_students(): # Function to view all student records
    if not students_records:
        print("No student records found.")
        return

    print("Student Records:")
    for student in students_records:
        print(f"ID: {student[0]}, Name: {student[1]}, Course: {student[2]}")


def search_student(): # Function to search for a student by ID
    student_id = input("Enter Student ID to search: ")
    for student in students_records:
        if student[0] == student_id:
            print(f"Student Found - ID: {student[0]}, Name: {student[1]}, Course: {student[2]}")
            return
    print("Student not found.")

def main(): # Main function to run the program
    while True:
        print("\nStudent Records Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()