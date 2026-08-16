
class atm_systm:
    def __init__(self,name,account_no,pin,balance):
        self.name = name
        self.account_no = account_no
        self.pin = pin
        self.balance =  balance
        self.transsaction = []

    def pin_check(self,pin):
        return pin == self.pin

    def ac_deatails(self):
        print("Account Holder:",self.name)
        print("Acoount Number:",self.account_no)
        print("Balance:",self.balance)

    def chk_bal(self):
        print("Curent Balance:",self.balance)

    def dpst(self,amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        self.balance += amount
        self.transsaction.append(f"Deposited {amount}")

        print("Amount Diposite:",amount)
        print("Balance:", self.balance)

    def withdraw(self,amount):

        if amount <= 0:
            print("Invalid Amount")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

            self.transsaction.append(f"Withdrawn {amount}")

            print("Withdrawn Amount",amount)
            print("Balance:",self.balance)

    def chng_pin(self,oldpin,newpin):
        if oldpin != self.pin:
            print("Incorrect Pin")
            return
        if newpin < 1000 or newpin > 9999:
            print("Pin must contain 4 digit")
            return
        self.pin = newpin

        print("Pin changed Successfully")

    def statement(self):
        if len(self.transsaction) == 0:
            print("No Transsactions")
        else:
            for transsaction in self.transsaction:
                print("-", transsaction)

        print("Current Balance:",self.balance)

account = atm_systm("Harsh", "987623457", 9644, 100000)

while True:
    print("""
ATM Menu

1. Account Details
2. Check Balance
3. Deposit Money
4. Withdraw 
5. Change Pin
6. Statement
7 Exit""")

    choice = int(input("Enter Your Choice: "))

    if choice ==  1:
        account.ac_deatails()

    elif choice == 2:
        account.chk_bal()

    elif choice == 3:
        amount = int(input("Enter Amount: "))
        account.dpst(amount)

    elif choice == 4:
        amount = int(input("Enter Amount: "))
        account.withdraw(amount)

    elif choice == 5:
        oldpin = int(input("Enter old pin: "))
        newpin = int(input("Enter New pin: "))

        account.chng_pin(oldpin, newpin)

    elif choice == 6:
        account.statement()

    elif choice == 7:

        print("Thank you for Using ATM")
        print("Please take your card")
        print("Have a nice day!")

        break

    else:
        print("Invalid Choice")




        
    
        

        