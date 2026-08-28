class Journel:
    """
    Definition: Manages personal journal entries using file handling.
    Arguments: None
    Return Value: None
    """
    def __init__(self):
        """
        Definition: Initializes the Journal Manager.
        Arguments: self
        Return Value: None
        """
        print("Welcome to Personal Journel Manager!")


    def __file(self):
        """
        Definition: Adds a new journal entry with date and time.
        Arguments: self
        Return Value: None
        """
        from datetime import datetime
        time = datetime.now()
        self.formated = time.strftime("[%Y-%m-%d %H-%M-%S]")
        print(self.formated)
        print("Enter Journal Entry:")
        entry=input("")
        with open("journalFile.txt", "a") as data:
            data.write(self.formated + "\n" + entry + "\n")

        print("Entery Added Successfully")

    def __fileview(self):
        """
        Definition: Reads and displays all journal entries from the file.
        Arguments: self
        Return Value: None
        """
        print("-------------------------------")
        try :
            with open("journalFile.txt", "r") as source:
                read= source.read()
                if read:
                    print(read)
                else:
                    print("No journal entries found.")
        except AttributeError:
            print("No Journal entries found. start by adding a new entry, The Journal file doesn't exist. please add new entry first.")

    def __searchentry(self):
        """
        Definition: Searches the journal file for a given keyword.
        Arguments: self
        Return Value: None
        """
        print("-------------------------------")
        try:
            searchitem = input("Enter Word:")

            with open("journalFile.txt", "r") as source:
                lst1 = source.readlines()
            found = False
            for line in lst1:
                if searchitem in line:
                    print(line.strip())
                    found = True
            if not found:
                print(f"No entries were found for the Keyword: {searchitem}")
                    
        except FileNotFoundError:
            print("N entries file exist yet")

    def __delentries(self):
        """
        Definition: Handles the option to delete all journal entries.
        Arguments: self
        Return Value: None
        """
        print("-------------------------------")
        try:
            with open("journalFile.txt", "r") as source:
                user = input("Are u Sure you want to delete all entries: ")

            if user == "Yes":
                print("All Journal Entries Have Been deleted")
                pass
            elif user == "No":
                print("Nice")
        except FileNotFoundError:
            print("No journal entries to delete")

    def jorunalmenu(self):
        
        while True:
            print("""Please Select an Option:
            1. Add New Entry
            2. View All Entries
            3. Search For an entry
            4. Delete All Entries """)
            choice =int(input("Enter Choice:"))
            if choice == 1:
                self.__file()
            elif choice == 2:
                self.__fileview()
            elif choice == 3:
                self.__searchentry()
            elif choice == 4:
                self.__delentries()
            elif choice == 5:
                print("Thank You for using Personal journal Manager. Goodbye!")

                print("Journel Class:")
                print(Journel.__doc__)
                
                print("\n__init__():")
                print(Journel.__init__.__doc__)
                
                print("\n__file():")
                print(Journel.__file.__doc__)
                
                
                print("\n__fileview:")
                print(Journel.__fileview.__doc__)

                print("\n__searchentry:")
                print(Journel.__searchentry.__doc__)

                print("\n__delentries:")
                print(Journel.__delentries.__doc__)

                break
            else:
                print("Invalid Option. Please select a valid option from Menu.")
            
            

Journel=Journel()
Journel.jorunalmenu()
 

    