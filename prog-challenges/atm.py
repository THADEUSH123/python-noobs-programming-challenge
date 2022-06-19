import random

class BankAccount:
    # Construct a BankAccount object
    def __init__(self, account_number, account_pin, balance=0.0):
        self.accountnum = int(account_number)
        self.balance = float(balance)
        self.pin = int(account_pin)
        self.account_locked = False

    def is_valid_pin(self, test_pin):
        if int(test_pin) == self.pin:
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than $0.00")
        elif self.balance >= float(amount):
            self.balance = self.balance - amount
            print("${} withdrawn from your account.".format(str(amount)))
        else:
            print("Withdrawal Error: Insuficient funds available.")

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + float(amount)
            print("${} added to your account.".format(str(amount)))
        else:
            print("Deposit Error: Deposits must be a positive value")



class ATM:
    #Create the mechanical ATM Class
    def __init__(self):
        self.accountregistry = {}

    def open_main_menu(self):
        active_account_number = None
        while True:
            print("\nWelcome to Hooverville Bank and Trust ATM. "
                  "Please select from the following options:\n"
                  "1 - Login\n"
                  "2 - Create Account\n"
                  "3 - Exit ATM")

            selection = input("Enter your selection: ")
            if selection == 1:
                active_account_number = self.attempt_login()
                if active_account_number:
                    self.open_account_menu(active_account_number)

            elif selection == 2:
                active_account_number = self.create_account()

            elif selection == 3:
                print("Thank you for using Hooverville Bank and Trust ATM. Goodbye.")
                exit()
            else:
                print("Your selection is invalid. Please enter 1, 2, or 3.")

    def attempt_login(self):
        ALLOWED_ATTEMPTS = 3
        while True:
            account_number = input("Please enter your 5 digit account "
                               "number or X to return to the main menu: ")

            if account_number == "X":
                return
            for x in range(ALLOWED_ATTEMPTS):
                account_pin = input("Please enter your 4 digit pin: ")
                if account_number not in self.accountregistry:
                    print("Not a valid account/pin combo. You have 3 attempts")
                elif self.accountregistry[account_number].is_valid_pin(account_pin):
                    print("Success!")
                    return account_number

            print("This account has been locked because the wrong pin was entered too many times.")
            return None

    def create_account(self):
        #Create a new account using a random number
        while True:
            pin = input("Please choose a 4 digit pin: ")
            if pin < 0 or pin > 9999:
                print("Pin must be 4 digits.")
            else:
                break

        while True:
            account_number = random.choice(range(10000,100000))
            if account_number not in self.accountregistry:
                break

        #Create account
        self.accountregistry[account_number] = BankAccount(account_number, pin, 0.00)
        print("Your account number is {}.\n Please record this number for "
              "future use.".format(str(account_number)))
        return account_number


    def open_account_menu(self, account_number):
        # Display the account menue and direct input to the user.
        while True:
            print("\nPlease select from the following options: \n"
                  "1 - Deposit\n"
                  "2 - Withdraw\n"
                  "3 - Check Balance\n"
                  "4 - Exit ATM\n")

            selection = input("Enter your selection: ")

            if selection is 1:
                account = self.accountregistry[account_number]
                amount = float(input("Enter amount to be Deposited: "))
                account.deposit(amount)

            elif selection is 2:
                account = self.accountregistry[account_number]
                amount = float(input("Enter amount to be Withdrawn: "))
                account.withdraw(amount)

            elif selection is 3:
                account = self.accountregistry[account_number]
                print("Your ballance is ${}.".format(str(account.get_balance())))

            elif selection is 4:
                print("Thank you for using Hooverville Bank and Trust ATM. Goodbye.")
                exit()
            else:
                print("Your selection is invalid. Please enter 1, 2, 3, or 4.")

atm = ATM()
atm.open_main_menu()
