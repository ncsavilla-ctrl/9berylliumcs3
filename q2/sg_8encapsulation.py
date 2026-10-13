class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self._balance = balance
        
        def set_account_number(self, account_number: int):
            self.__account_number = account_number
            
        def set_balance(self, balance: float):
            if balance < 0:
                print("The balance must not be a negative number.")
                
            else:
                self.__balance = balance
                
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    def display_info(self, label: str = ""):
        if label:
            print(label)
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f}\n")
        
    if __name__ == "__main__":
        a1 = BankAccount(12345, 1000)
        print("Output: ")
        a1.display_info("Account 1")
        
    print("Update balance to -100")
    a1.set_balance(-100)
    a1.display_info()
    
