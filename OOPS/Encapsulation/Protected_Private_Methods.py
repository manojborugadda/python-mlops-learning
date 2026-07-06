
class Bank_Account:
    def __init__(self, balance=0):
        self.balance = balance

    def _show_balance(self): # protected method
        print(f"Balance: {self.balance}")
    
    def __update_balance(self,amount): # private method
        self.balance += amount
    
    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print("invalid deposit amount")
    
amount = Bank_Account(500)  # Initialize with a balance of 500
amount._show_balance()
# amount.__update_balance(100)  # This will raise an AttributeError
amount.deposit(100)  # Valid deposit

    