### personal finance calculator
#input
inc=input("enter monthly income:")
inc=int(inc)
rent=input("enter monthly rent:")
rent=int(rent)
food=input("enter food expense:")
food=int(food)
trpt=input("enter monthly transport expense:")
trpt=int(trpt)
ent=input("enter entertainment expense:")
ent=int(ent)
misc=input("enter other expenses:")
misc=int(misc)

#calculation+output
print(f"Your total expense:{rent+food+trpt+ent+misc}")
print(f"Your savings:{inc-(rent+food+trpt+ent+misc)}")
savings=inc-(rent+food+trpt+ent+misc)
print(f"Your savings %:{(savings/inc)*100}")

#output(financial health)
sr=(savings/inc)*100  #sr=savings ratio
if sr>=30:
    (print("Excellent financial discipline!"))
elif 15<sr<30:
    (print("Good, Keep improving."))
elif sr<=15:
    (print("You should redude your expenses"))