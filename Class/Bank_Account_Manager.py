class Bank:
    #class variable
    balance = 0

    def __init__(self, Name):
        self.name = Name 
        print(f'Hello {self.name}. Welcome to our banking Facility')

    def deposit_cash(self):
        amount = int(input("Enter amount to be deposited: "))
        self.balance += amount
        print(f'Available balance is : {self.balance} \n')

    def withdrawal(self):
        withdraw_amount = int(input("Enter withdrawan amount: "))

        if self.balance >= withdraw_amount :
            print(f'\nWithdrawl amount : {withdraw_amount} \n')
            self.balance -= withdraw_amount
            print(f"Updated balance : {self.balance} \n")
        else:
            print(f'Insufficient amount ')
            print(f"Available balance to withdraw : {self.balance} \n")
 
    def show_balance(self):
        print(f"Available balance is : {self.balance} \n")


