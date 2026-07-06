#exc1
age=input("Enter your age:")
age=int(age)
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#exc2
mark=input("Enter your marks:")
mark=int(mark)
if 90< mark <= 100:
    print("Grade:A")
elif 80< mark <= 90:
    print("Grade:B")
elif 70<mark<=80:
    print("Grade:C")
elif 60<mark<=70:
    print("Grade:D")
else:
    print("Failed")

#exc3
sal= input("Enter your Salary:")
sal=int(sal)
if sal>100000:
    print("High income")
elif sal>50000:
    print("Middle income")
else:
    print("Starting Out")
