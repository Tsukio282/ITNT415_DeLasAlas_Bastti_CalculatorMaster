# calculator.py

def add(num1, num2):
    def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    # To be implemented in the subtraction branch
    pass

def multiply(num1, num2):
    # To be implemented in the multiplication branch
    pass

def divide(num1, num2):
    # To be implemented in the division branch
    pass

def main():
    # ANSI color codes for the UI
    PINK = '\033[38;5;206m'
    PURPLE = '\033[38;5;99m'
    RESET = '\033[0m'

    while True:
        print(f"\n{PINK}=== PURPLE CALCULATOR MENU ==={RESET}")
        print(f"{PURPLE}1. Add{RESET}")
        print(f"{PURPLE}2. Subtract{RESET}")
        print(f"{PURPLE}3. Multiply{RESET}")
        print(f"{PURPLE}4. Divide{RESET}")
        print(f"{PURPLE}5. Exit{RESET}")

        choice = input(f"{PINK}Select operation (1/2/3/4/5): {RESET}")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        else:
            print("Invalid Input. Please select a valid menu option.")

if __name__ == "__main__":
    main()