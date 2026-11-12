import util

students = []

# Add a new student
def add_student():
    print("\n---- Add New Student ----")
    name = input("Enter student name: ")
    reg_no = input("Enter Student Registration Number: ")
    student = {
        "name": name,
        "reg_no": reg_no,
        "marks": [],
        "average": 0,
        "grade": "N/A"
    }

    students.append(student)
    print("Student added successfully!")

    #Viewing the students records
    def view_students():
        print("\n---- Student Records ----")
        if len(students) == 0:
            print("No students found.")
            return
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Registration Number: {student['reg_no']}")
            print(f"Marks: {', '.join(map(str, student['marks']))}")
            print(f"Average: {student['average']}")
            print(f"Grade: {student['grade']}")
            
#Searching Student function
def search_student():
    print("\n---- Search Student ----")
    reg_no = input("Enter Student Registration Number: ")
    for student in students:
        if student["reg_no"] == reg_no:
            print(f"Name: {student['name']}")
            print(f"Registration Number: {student['reg_no']}")
            print(f"Marks: {', '.join(map(str, student['marks']))}")
            print(f"Average: {student['average']}")
            print(f"Grade: {student['grade']}")


#Adding marks for the student
def add_marks():
    print("\n---- Add Marks ----")
    reg_no = input("Enter Student Registration Number: ")
    for student in students:
        if student["reg no"] == reg_no:
            try:
                m1 = int(input("Enter marks for English: "))
                m2 = int(input("Enter marks for Maths: "))
                m3 = int(input("Enter marks for English: "))
                student["marks"] = [m1, m2, m3]
                student["average"] = sum(student["marks"]) / len(student["marks"])
                student["grade"] = util.calculate_grade(student["average"])
                print("Marks added successfully!")
            except ValueError:
                print("Invalid input. Marks should be integers.")
            return
        else:
            print("Student not found")


#Deletion of the student
def delete_student():
    print("---- DELETE STUDENT ----")
    reg = input("Enter Student Registration Number: ")
    for s in students:
        if s["reg_no"] == reg:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found.")

#Saving to file
def save_to_file():
    print("---- Saving The Data To The File--file_name = students.txt ----")
    try:
        file = open("students_data.txt", "w")

        for s in students:
            data = f"{s['name']},{s['marks']},{s['average']},{s['grade']}\n"
            file.write(data)
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving data: {e}")

#loading of the file
def load_from_file():
    print("---- Loading Data From File ----")
    file = open("students_data.txt", "r")
    students.clear()
    for line in file:
        data = line.strip().split(",")
        student = {
            "name": data[0],
            "reg_no": data[1],
            "marks": data[2],
            "average": data[3],
            "grade": data[4],
        }

        students.append(student)

    file.close()
    print("Data loaded successfully!")
            