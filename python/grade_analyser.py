def get_marks():
    marks=[]
    n=5
    while n>0:
        x=int(input("Enter marks:"))
        marks.append(x)
        n=n-1
    return(marks)
def calc(ls):
    total=0
    highest=ls[0]
    lowest=ls[0]
    passcount=0
    for i in ls:
        total=total+i
        if(highest<i): highest=i
        if (lowest>i): lowest=i
        if(i>=40): passcount=passcount+1
    print(f"Total:{total}")
    print(f"Average:{total/len(ls)}")
    print(f"Highest:{highest}")
    print(f"Lowest:{lowest}")
    print(f"Passed Subjects:{passcount}")
    average=total/len(ls)
    if(average>=90):print("average grade is A+")
    elif(average>=80):print("average grade is A")
    elif(average>=70):print("average grade is B")
    elif(average>=60):print("average grade is C")
    elif(average>=40):print("average grade is D")
    else:print("average grade is F")
m=get_marks()
calc(m)
