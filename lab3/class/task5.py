class account:
    owner=None
    balance=0

    def deposit(self, x):
        self.balance+=x
        print("Your balance: ", self.balance)

    def withdraw(self, x):
        if x>self.balance:
            print("Error, it must not exceed the balance")
        else:
            self.balance=self.balance-x
            print("Your balance: ", self.balance)


a=account()
q=""
while q!="quit":
    q=str(input())
    if q=="deposit":
        print("Amount of cash that you want to append: ")
        a.deposit(int(input()))
    elif q=="withdraw":
        print("Amount of cash that you want to withdraw: ")
        a.withdraw(int(input()))
    
