#ATM interface
#Task 1

class ATM:
    def __init__(self):
        self.balance = 10000.0
        self.pin = "1234"
        self.transaction_history = []

   
    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    
    def cash_withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount:.2f}")
        print(f"You have successfully withdrawn: ${amount:.2f}")

   
    def cash_deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")
        print(f"You have successfully deposited: ${amount:.2f}")

    
    def change_pin(self, new_pin):
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("New PIN must be a 4-digit number.")
            return
        self.pin = new_pin
        print("PIN changed successfully.")

    
    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions found.")
            return
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
 atm = ATM()
atm = ATM()


import time

print("Please insert your CARD")

time.sleep(5)

password=1432

pin=int(input("Enter your ATM Pin:"))
 
if pin==password:   
    while True:
        print("\nATM Interface")
        print("1. Check Balance")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        
        choice = input("Select an option: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            atm.cash_withdrawal(amount)
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            atm.cash_deposit(amount)
        elif choice == "4":
            new_pin = input("Enter new 4-digit PIN: ")
            atm.change_pin(new_pin)
        elif choice == "5":
            atm.show_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

else:
  
  print("Wrong pin, Please try again")


if __name__ == "__main__":
    main()
