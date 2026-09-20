import datetime
import time
import math
import random
import uuid
import filemodule


def display_time():
    """
    This function displays the current date and time.
    Arguments: None
    Returns: None
    """
    current = datetime.datetime.now()
    print("Current Date and Time:", current)


def date_difference():
    """
    This function calculates the difference between two dates.c
    Arguments: None
    Returns: None
    """
    print("Enter first date YYYY-MM-DD:")
    first = input()

    print("Enter second date YYYY-MM-DD:")
    second = input()

    date1 = datetime.datetime.strptime(first, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(second, "%Y-%m-%d")

    difference = date2 - date1

    print("Difference in days:", difference.days)


def format_date():
    """
    This function displays the date in custom format.
    Arguments: None
    Returns: None
    """
    current = datetime.datetime.now()

    formatted = current.strftime("%d %B %Y")

    print("Formatted Date:", formatted)


def stopwatch():
    """
    This function runs a simple stopwatch.
    Arguments: None
    Returns: None
    """
    print("Press Enter to start")
    input()

    start = time.time()

    print("Press Enter to stop")
    input()

    end = time.time()

    elapsed = end - start

    print("Time Passed:", elapsed, "seconds")


def countdown():
    """
    This function runs a countdown timer.
    Arguments: None
    Returns: None
    """
    seconds = int(input("Enter seconds: "))

    while seconds > 0:
        print(seconds)

        time.sleep(1)

        seconds -= 1

    print("Time is Over!")


def factorial_calc():
    """
    This function calculates the factorial of a number.
    Arguments: None
    Returns: None
    """
    number = int(input("Enter number: "))

    result = math.factorial(number)

    print("Factorial:", result)


def trig_calc():
    """
    This function calculates the sine of an angle.
    Arguments: None
    Returns: None
    """
    angle = float(input("Enter angle: "))

    result = math.sin(angle)

    print("Sine Value:", result)


def compound_interest():
    """
    This function calculates compound interest.
    Arguments: None
    Returns: None
    """
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate: "))
    years = float(input("Enter years: "))

    amount = principal * math.pow(
        (1 + rate / 100),
        years
    )

    print("Final Amount:", amount)


def circle_area():
    """
    This function calculates the area of a circle.
    Arguments: None
    Returns: None
    """
    radius = float(input("Enter radius: "))

    area = math.pi * radius * radius

    print("Circle Area:", area)


def random_number():
    """
    This function generates a random number.
    Arguments: None
    Returns: None
    """
    number = random.randint(1, 100)

    print("Random Number:", number)


def random_list():
    """
    This function selects random items from a list.
    Arguments: None
    Returns: None
    """
    items = [
        "Cricket",
        "Minecraft",
        "Burger",
        "Watch",
        "Laptop"
    ]

    result = random.sample(items, 2)

    print("Random Items:", result)


def random_password():
    """
    This function generates a random password.
    Arguments: None
    Returns: None
    """
    length = int(input("Enter password length: "))

    characters = "qwertyuiopasdfghjkl1234567890"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


def random_otp():
    """
    This function generates a random OTP.
    Arguments: None
    Returns: None
    """
    otp = random.randint(1000, 9999)

    print("Generated OTP:", otp)


def generate_uuid():
    """
    This function generates a unique UUID.
    Arguments: None
    Returns: None
    """
    unique_id = uuid.uuid4()

    print("Generated UUID:", unique_id)


def explore_module():
    """
    This function displays attributes of a selected module.
    Arguments: None
    Returns: None
    """
    print("Available Modules: math, random, time")

    module_name = input("Enter module name: ")

    if module_name == "math":
        print(dir(math))

    elif module_name == "random":
        print(dir(random))

    elif module_name == "time":
        print(dir(time))

    else:
        print("Module not available")


def show_documentation():
    """
    This function displays documentation of project functions.
    Arguments: None
    Returns: None
    """
    print(display_time.__doc__)
    print(date_difference.__doc__)
    print(format_date.__doc__)
    print(stopwatch.__doc__)
    print(countdown.__doc__)

    print(factorial_calc.__doc__)
    print(trig_calc.__doc__)
    print(compound_interest.__doc__)
    print(circle_area.__doc__)

    print(random_number.__doc__)
    print(random_list.__doc__)
    print(random_password.__doc__)
    print(random_otp.__doc__)

    print(generate_uuid.__doc__)
    print(explore_module.__doc__)

    print(filemodule.make_file.__doc__)
    print(filemodule.write_file.__doc__)
    print(filemodule.read_file.__doc__)

    print(main.__doc__)


def main():
    """
    This function runs the main menu of the toolkit.
    Arguments: None
    Returns: None
    """

    running = True

    while running:

        print("""
====================================
       MULTI UTILITY TOOLKIT
====================================

1. Date and Time
2. Mathematics
3. Random
4. UUID
5. File Operations
6. Explore Module
7. Exit
""")

        choice = input("Enter your choice: ")

        # Date and Time
        if choice == "1":

            print("""
1. Current Time
2. Date Difference
3. Custom Date Format
4. Stopwatch
5. Countdown
""")

            option = input("Enter option: ")

            if option == "1":
                display_time()

            elif option == "2":
                date_difference()

            elif option == "3":
                format_date()

            elif option == "4":
                stopwatch()

            elif option == "5":
                countdown()

            else:
                print("Invalid Option")


        # Mathematics
        elif choice == "2":

            print("""
1. Factorial
2. Compound Interest
3. Circle Area
4. Trigonometry
""")

            option = input("Enter option: ")

            if option == "1":
                factorial_calc()

            elif option == "2":
                compound_interest()

            elif option == "3":
                circle_area()

            elif option == "4":
                trig_calc()

            else:
                print("Invalid Option")


        # Random
        elif choice == "3":

            print("""
1. Random Number
2. Random Password
3. Random OTP
4. Random List
""")

            option = input("Enter option: ")

            if option == "1":
                random_number()

            elif option == "2":
                random_password()

            elif option == "3":
                random_otp()

            elif option == "4":
                random_list()

            else:
                print("Invalid Option")


        # UUID
        elif choice == "4":

            generate_uuid()


        # File
        elif choice == "5":

            print("""
1. Create File
2. Write File
3. Read File
""")

            option = input("Enter option: ")

            if option == "1":
                filemodule.make_file()

            elif option == "2":
                filemodule.write_file()

            elif option == "3":
                filemodule.read_file()

            else:
                print("Invalid Option")


        # Module Exploration
        elif choice == "6":

            explore_module()


        # Exit
        elif choice == "7":

            print("\nThank you for using Multi Utility Toolkit!")
            print("Goodbye!")

            show_documentation()

            running = False


        else:

            print("Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()