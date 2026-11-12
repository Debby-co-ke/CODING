# Utility functions module

def print_menu():
    print("|n===== STUDENT ACADEMIC MANAGEMENT SYSTEM=====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Add Marks")
    print("5. Save Records to file")
    print("6. Load Records from file")
    print("7. Delete Student")
    print("8. Exit")


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
