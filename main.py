# main.py
import student_operations as ops

def display_menu():
    print("\n" + "="*30)
    print("  STUDENT MANAGEMENT SYSTEM  ")
    print("="*30)
    print("1. Add a New Student")
    print("2. View All Students")
    print("3. Update a Student's Course")
    print("4. Delete a Student")
    print("5. Exit")
    print("="*30)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email Address: ")
            course = input("Enter Course Name: ")
            ops.add_student(first_name, last_name, email, course)

        elif choice == '2':
            ops.view_students()

        elif choice == '3':
            try:
                student_id = int(input("Enter Student ID to update: "))
                new_course = input("Enter the new Course Name: ")
                ops.update_student_course(student_id, new_course)
            except ValueError:
                print("\nInvalid input. Student ID must be a number.")

        elif choice == '4':
            try:
                student_id = int(input("Enter Student ID to delete: "))
                # Add a simple confirmation guard
                confirm = input(f"Are you sure you want to delete ID {student_id}? (y/n): ")
                if confirm.lower() == 'y':
                    ops.delete_student(student_id)
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("\nInvalid input. Student ID must be a number.")

        elif choice == '5':
            print("\nExiting Student Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()