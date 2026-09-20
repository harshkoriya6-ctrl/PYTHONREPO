def make_file():
    """
    This function creates a file.
    Arguments: None
    Returns: None
    """
    filename = input("Enter file name: ")

    with open(filename, "w") as file:
        print("File Created Successfully")


def write_file():
    """
    This function writes data into a file.
    Arguments: None
    Returns: None
    """
    filename = input("Enter file name: ")
    text = input("Enter text: ")

    with open(filename, "a") as file:
        file.write(text + "\n")

    print("Data Written Successfully")


def read_file():
    """
    This function reads data from a file.
    Arguments: None
    Returns: None
    """
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            data = file.read()
            print("\nFile Content:")
            print(data)

    except FileNotFoundError:
        print("File not found")