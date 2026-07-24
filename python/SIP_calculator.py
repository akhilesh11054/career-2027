#SIP Calculator

#input values
mon_inv=input("Enter monthly investment amount:") #mon_inv - monthly investment 
mon_inv=int(mon_inv)
ret=input("Enter annual return % :")
ret=int(ret)
yrs=input("Enter investment time years:")
yrs=int(yrs)

#calculation
tot_inv = mon_inv*12*yrs

#output
print(f"Total invested amount:{tot_inv}")