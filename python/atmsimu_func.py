balance=10000
def checkbal():
    print(f"Your current balance is {balance}")
def deposit(x):
    global balance
    balance=balance+x
    print(f"Deposit of Rs.{x} is successful\nYour current balance is{balance}")
def withdraw(y):
    global balance
    if(y>balance):
        print("Insufficient Balance!")
    else:
        balance=balance-y
        print(f"Withdrawal of Rs.{y} is successful\nYour current balance is {balance}")
def mainloop():
    while True:
        cho=int(input("Choose an option:\n\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit\n>"))
        if(cho==1):
            checkbal()
        elif(cho==2):
            dep=int(input("Enter deposit amount:"))
            deposit(dep)
        elif(cho==3):
            wid=int(input("Enter withdrawal amount:"))
            withdraw(wid)
        elif(cho==4):
            print("Thank you!")
            break
        else:
            print("Invalid Entry")
mainloop()