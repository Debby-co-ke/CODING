import util
import student_module


#Entry point for the whole program
def main():
    while True:
        util.print_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            student_module.add_student()
        elif choice == "2":
            student_module.view_student()
        elif choice == "3":
            student_module.search_student()
        elif choice == "4":
            student_module.add_marks()
        elif choice == "5":
            student_module.save_to_file()
        elif choice == "6":
            student_module.load_from_file()
        elif choice == "7":
            student_module.delete_student()

        return
main()
