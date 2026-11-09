class LunchCard:
    def __init__(self, ID, name, initial_balance=0):
        self.ID = ID
        self.myName = name
        self.balance = initial_balance
    
    def payLunch(self, bill_amount):
        if isinstance(bill_amount, int) or isinstance(bill_amount, float):
            if self.balance >= bill_amount:
                self.balance -= bill_amount
                print("Payment was done for", self.myName)
            else:
                print("Your balance is not sufficient!")
        else:
            print("bill_amount must be a numerical value!")

    def depositMoney(self, amount):
        if isinstance(amount, int) or isinstance(amount, float):
            if amount > 0:
                self.balance += amount
                self.DisplayCurrentBalance()
            else:
                print("Amount must be a positive numerical value!")
        else:
            print("Amount must be a numerical value!")

    def DisplayCurrentBalance(self):
        print("current balance for", self.myName, "with ID:", self.ID, "is", self.balance)