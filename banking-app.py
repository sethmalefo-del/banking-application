class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self._balance = initial_balance
    # Encapsulation: _balance is private to prevent direct external modification

    # Get method to access the private balance safely
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print(f"Deposited amount should be positive.")
            
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrew: ${amount: .2f}")
            
#Inherit: SavingAccount inherits from BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0.0, interest_rate=0.02):
        super().__init__(account_holder, initial_balance)           
        self.interest_rate = interest_rate #E.g 0.02 for 2% in calculations
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Calculated Interest ({self.interest_rate * 100}%): ${interest:.2f}")
        return interest
# --Testing the Implementations ---                                                  
if __name__ == "__main__":
    print("--- Creating Saving Account ---")
    my_account = SavingsAccount("John Smith", 1000.0, 0.05)
    print(f"Initial Balance: ${my_account.get_balance():.2f}")

    print("\n-- Performing transactions ---")
    my_account.deposit(500.0)
    print(f"Current balance: ${my_account.get_balance():.2f}")
    my_account.withdraw(200.0)
    print(f"Current Balance: ${my_account.get_balance():.2f}")
    my_account.withdraw(200.0)  # Attempting to overdraw

    print("--- Calculating Interest ---")
    interest_earned = my_account.calculate_interest()
    my_account.deposit(interest_earned)   #Adding interest to the balance.
    print(f"Final balance: ${my_account.get_balance():.2f}")
            