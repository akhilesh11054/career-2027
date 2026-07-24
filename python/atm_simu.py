bal=10000
while True:
    print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    x=int(input("Enter:"))
    if(x==1):
        print(f"Balance:{bal}")
    elif(x==2):
        dep=int(input("Enter deposit amount:"))
        bal=bal+dep
        print(f"{dep}, has been deposited.\nCurrent Balance:{bal}")
    elif(x==3):
        wid=int(input("Enter withdrawal amount:"))
        if wid<=bal:
            bal=bal-wid
            print(f"{wid}has been withdrawn\nCurrent Balance:{bal}")
        else:
            print("Insufficient Balance")
    elif(x==4):
        print("Thank you")
        break
    else:
        print("Invalid Entry")
        
    





