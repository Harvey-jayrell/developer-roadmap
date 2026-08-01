import os
students = []

def clear_screen():
    os.system("cls" if os.name =="nt" else "clear")

def show_menu():
    print("""
    ===============================
    Student Grade Management System
    ===============================
    1. add Student
    2. View Student
    3. Search Student
    4. Update Grade
    5. Delete Student
    6. Exit
    """)

def add_student():
    while True:
        try:
            name = input("Enter your name: ").strip()
            if not name: 
                print("Name cannot be empty.")
                continue
            grade = float(input("Enter your grade: "))
            if grade < 0 or grade > 100:
                            print("Grade must be between 0-100.")
                            continue
            student = {
                "name": name,
                "grade": grade
            
            }
            students.append(student)
            print("Student Added Successfully!")
            break
        except ValueError:
            print("Error: Invalid Input. Please enter numeric values.")


def view_students():
    if not students:
        print ("No Student Record!")
        return
    
    for student in students:
        print("name: ", student["name"])
        print("grade: ", student["grade"])
        print()

def search_student():

    search_name = input("Enter your Name: ").strip().lower()
    found = False
    if not students:
         print("No Student Record.")
         return
         
    
    for student in students:
        
        if search_name.lower() == student["name"].lower():
             found = True
             print("Student found.")
             print("name: ", student["name"])
             print("grade:",student["grade"] )
             print()
             break
    if not found:
        print("Student not Found.")
        return

def update_grade():
    search_name = input("Enter your Name: ").strip().lower()
    found = False
    if not students:
         print("No Student Record.")
         return

    for student in students:
         if search_name.lower() == student["name"].lower():
              found = True
              print("Student found.")
              while True:
                        try:
                            new_grade = float(input("Enter New Grade: "))
                            if new_grade < 0 or new_grade > 100:
                                print("Grade Must be 0-100.")
                                continue
              
                            student["grade"] = new_grade

                            print("Grade Updated Successfully.")
                            break
                        except ValueError:
                            print("Please Enter a valid number.")
                            
              
    if not found:
         print("Student not Found.")
         return
def delete_student():
    search_name = input("Enter your Name: ").strip().lower()
    found = False
    if not students:
        print("No Student Record.")
        return

    for student in students:
         if search_name.lower() == student["name"].lower():
            found = True
            print("Student found.")
            students.remove(student)
            print("Student Removed.")
            break

    if not found:
         print("Student not Found.")
def pause():
    input("Press Enter to Continue.")


def main():
    while True:
        clear_screen()

        show_menu()

        choice = input("Select an operation (1-6): ")
        if choice == "6":

            print("Exiting the System.")
            break
        if choice == "1":
            add_student()
            pause()

        elif choice == "2":
            view_students()
            pause()

        elif choice == "3":
             search_student()
             pause()

        elif choice == "4":
             update_grade()
             pause()
        elif choice == "5":
            delete_student()
            pause()

if __name__ == "__main__":
    main()

