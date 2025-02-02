import numpy as np

name = input("Enter your name: ").strip().capitalize()
firstname = name.split()[0]

ask = input(f"Hello, {firstname}, do you want to create a matrix? (yes/no): ").strip().lower()
while True:
    try:
        if ask == "yes":
            cols = int(input("Enter the number of columns: "))
            rows = int(input("Enter the number of rows: "))

            array = np.random.random((rows, cols)).round(20)
            print("Generated Matrix:")
            print(array)

            ask2 = input(
                f"{firstname}, do you want to perform any operation? (yes/no): ").strip().lower()

            while ask2 == "yes":
                print("""
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                """)

                get = input(
                    "Enter the operation number or name: ").strip().lower()

                if get in ["1", "addition"]:
                    print("Result of Addition:")
                    print(array + array)
                elif get in ["2", "subtraction"]:
                    print("Result of Subtraction:")
                    print(array - array)
                elif get in ["3", "multiplication"]:
                    print("Result of Multiplication:")
                    print(array * array)
                elif get in ["4", "division"]:
                    print("Result of Division:")
                    print(np.divide(array, array, out=np.zeros_like(
                        array), where=array != 0))
                else:
                    print("Invalid option, please try again.")

                ask2 = input(
                    "Do you want to perform another operation? (yes/no): ").strip().lower()

            break 

        elif ask == "no":
            print("Okay, have a great day!")
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
            ask = input(
                "Do you want to create a matrix? (yes/no): ").strip().lower()

    except ValueError:
        print("Invalid input, please enter a valid number.")
