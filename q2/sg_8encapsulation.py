class BankAccount: # This creates the parent class named BankAccount
    def __init__(self, account_number: int, balance: float): # This initializes the account numbebr and its balance
        self.__account_number = account_number # This stores the given account number
        self.__balance = balance # This stores the account balance

    def set_account_number(self, account_number: int): # This is a setter for the account number
        self.__account_number = account_number # This stores the account number

    def set_balance(self, balance: float): # This is a setter for the balance
        if balance < 0: # If the number is less than 0 it will lead to an error
            print("The balance must not be a negative number.") # If the input was negative, this will print that the balance shouldn't be negative
        else: # If the number isn't negative, it will result to this
            self.__balance = balance # This stores the balance

    @property # This is a decorator that is used to define a method as a property that allowing it to be accessed like an attribute
    def account_number(self): # This is the getter method for the account number
        return self.__account_number # This returns the value

    @property # This is a decorator that is used to define a method as a property that allowing it to be accessed like an attribute
    def balance(self): # This is the getter method for the balance
        return self.__balance # This returns the value

    def display_info(self, label: str = ""): # This defines a method named display_info that belongs to the class
        if label: # This checks if label contains a value
            print(label) # Prints the label
        print(f"Account Number: {self.account_number}") # This prints the account number
        print(f"Balance: {self.balance:.2f}\n") # This prints the balance



    a1 = BankAccount(12345, 1000) # This creates an object named a1 from the BankAccount class

    print("Output:") # This prints the output
    a1.display_info("Account 1") # This calls the method display_info using the a1 object

    print("Update balance to -100") # This prints the update balance
    a1.set_balance(-100) # This calls the method st_balance using the a1 object
    a1.display_info() # This calls the method display_info using the a1 object
