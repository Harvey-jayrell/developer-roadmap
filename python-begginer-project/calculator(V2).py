import os
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    print("""
    ====================
    Simple Calculator
    ====================
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    """)
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
    
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter your first Number: "))
            num2 = float(input("Enter your Second Number: "))
            return num1, num2
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
def pause():
    input("Press Enter to Continue...")

def main():

    while True:
            clean_screen()
            show_menu()
            choice = input("Select an operation (1-5): ")
            if choice == '5':
                print("Exiting the Calculator. Goodbye!")
                break
            elif choice in ['1', '2', '3', '4']:
                num1, num2 = get_numbers()

                if choice == '1':
                    result = addition(num1, num2)

                elif choice == '2':
                    result = subtraction(num1, num2)
                    
                elif choice == '3':
                    result = multiplication(num1, num2)

                elif choice == '4':
                    result = division(num1, num2)

                print("The result is: ", result)
                pause()

            else:
                print("Invalid input.")
                pause()


if __name__ == "__main__":
    main()
