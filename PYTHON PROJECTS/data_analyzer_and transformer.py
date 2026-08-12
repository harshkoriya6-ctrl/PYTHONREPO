
data = []
data_t = 0
ttl = 0
ovrl = 0


def in_data():
    """1. in_data():
Definition: Takes and stores 1D or 2D array data from the user.
Arguments: None.
Return Value: None."""

    global data, data_t, ttl, ovrl

    print("Enter Your Choice:")
    print("""
1. 1D Array Data
2. 2D Array Data
""")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
         data = list(map(int, input("Enter data: ").split()))
         data_t = 1

    elif choice == 2:
         row = int(input("Enter the number of Rows: "))
         col = int(input("Enter the number of Columns: "))

         data = []

         for i in range(row):
            row_data = list(map(int, input(f"Enter row {i + 1}: ").split()))

            if len(row_data) != col:
                print(f"Please enter exactly {col} values.")
                return

            data.append(row_data)

         data_t = 2

         print("2d Array is:")
         print(data)

    else:
        print("Invalid Choice")
        return

    ttl = len(data)

    print("Data has been stored successfully!")


def summary_data():
    """2. summary_data()
Definition: Displays the summary of the stored dataset.
Arguments: None.
Return Value: None."""

    print("""Which Array is Stored
    1. 1D Array
    2. 2D Array
    3. Clear Data""")
  
    data_t = input("Enter The choice: ")
    if data_t == "1":
         print(f""""Data Summary:
               - Total Elements:{len(data)}
               - Minimum Value: {min(data)}
               - Sum of all Elements: {sum(data)}
               - Average Value: {sum(data)/len(data)}""")
         
    elif data_t == "2":

        total = sum(len(row)for row in data)
        total_sum = sum(sum(row)for row in data)
        minimum = min(min(row)for row in data)
        average = total_sum / total 
       
        print(f"""
    Data Summary:
    - Total Elements: {total}
    - Minimum Value: {minimum}
    - Sum of all Elements: {total_sum}
    - Average Value: {average:.2f}""")

def factorial_calc(n):
    """3.factorial_calc(n): 
Definition: Calculates the factorial of a given number using recursion.
Arguments: n - Number whose factorial is calculated.
Return Value: Factorial of n."""

    if n < 0:
        print("Factorial is not Possible for nagative value")
        return  

    if n == 0 or n == 1:
        return 1
    return n*factorial_calc(n-1)

def filter_data(row, threshold):
    """4. filter_data(row, threshold):
Definition: Filters array values greater than or equal to the threshold.
Arguments: row – Array, threshold – Minimum value.
Return Value: Filtered list."""

    result = list(filter(lambda a : a >= threshold, row))
    return result


def sort_data():
    """5. sort_data():
Definition: Sorts the stored array in ascending or descending order.
Arguments: None.
Return Value: None."""
    if data_t == 1:
        print("""
        \nChoose Sorting Option
1. Ascending
2. Dscending""")

        choice = int(input("Enter Choice: "))
        if choice == 1:
            data.sort()
            print("Data in acending Order:")
            print(*data, sep=", ")
        elif choice == 2:
            data.sort(reverse=True)
            print("Data in Decending Order:")
            print(*data, sep=", ")
        else:
            print("invalid choice")

    elif data_t == 2:

        print("""
                \nChoose Sorting Option
        1. Ascending
        2. Dscending""")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            sort_data = [sorted(row) for row in data]

            print("2D Array in Ascending:")

            for row in sort_data:
                print(*row, sep=" ")

        elif choice == 2:
            sort_data = [sorted(row, reverse=True) for row in data]

            print("2D Array in Descending:")

            for row in sort_data:
                print(*row, sep=" ")

        else:
            print("Invalid Choice")


def stat_data():
    """6. stat_data()
Definition: Calculates basic statistics of the stored 1D dataset.
Arguments: None.
Return Value: Minimum, maximum, average, and total."""
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total/len(data)

    return minimum, maximum, average, total

print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("""
Main Menu:

1. Input Data
2. Display the Data Summary (Built In Function)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
""")

    userin = input("Please Enter Your Choice: ")

    if userin == "1":
        in_data()

    elif userin == "2":
         summary_data()

    elif userin == "3":
        n = int(input("Enter Number for factorial: "))
        result = factorial_calc(n)
        print(f"Factorial of {n} is:", result)

    elif userin == "4":
        if len(data) == 0:
            print("Please enter data")
            continue

        threshold = int(input("Enter Value: "))

        if data_t == 1:

            result = filter_data(data, threshold)

            print(f"Filtered Data {threshold}")

            if len(result) > 0:
                print(*result, sep=", ")
            else:
                print("Values Not Found")

        else:
            result = [filter_data(row, threshold)
                      for row in data]
            print(f"Filtered Data {threshold}:")

            for row in result:
                print(*row, sep=", ")

    elif userin == "5":
        if len(data) == 0:
            print("Enter Data: ")
            continue
        sort_data()
            
    elif userin == "6":
        if len (data) == 0:
            print("Please enter data:")
            continue
        if data_t == 1:
            mini, maxi, average, total = stat_data()
        else:
            mini = min(min(row)for row in data)
            maxi = max(max(row)for row in data)
            total = sum(sum(row)for row in data)
            count = sum(len(row)for row in data)
            average = total / count

            print("Dataset Statistics: ")
            print("- Minimum value:",mini)
            print("- Maximum value:",maxi)
            print("- Total value:",total)
            print("- Average value:",f"{average: .2f}")
    
    elif userin == "7":
        print("Thank youu for using the Data Analyzer. Goodbye!")
        print("UDF 1: ",in_data.__doc__)
        print("UDF 2: ",summary_data.__doc__)
        print("UDF 3:",factorial_calc.__doc__)
        print("UDF 4:",filter_data.__doc__)
        print("UDF 5:",sort_data.__doc__)
        print("UDF 6:",stat_data.__doc__)
        break
         


    else:
        print("Invalid Choice")
