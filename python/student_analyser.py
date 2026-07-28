def get_inp():
    n=5
    name=list()
    mark=list()
    while (n>0):
        nam=input('enter student name:')
        name.append(nam)
        mar=int(input('enter student marks:'))       
        mark.append(mar)
        n=n-1
    return(name,mark)
def grade_analyser(m):
    grade=list()
    for i in range(len(m)):
        if(m[i]>=90): grade.append("Grade A+")
        elif(m[i]>=80):grade.append("Grade A")
        elif(m[i]>=70):grade.append("Grade B")
        elif(m[i]>=60):grade.append("Grade C")
        elif(m[i]>=40):grade.append("Grade D")
        else:grade.append("Grade F")
    return(grade)

def calc(n,m,g):
    passcount=0
    print("\n-----STUDENT PERFORMANCE-----\n")
    for i in range(len(n)):
        print(f'{n[i]} - {m[i]} - {g[i]}')
        if (m[i]>=40):
            passcount=passcount+1
    average=sum(m)/len(m)
    highest=max(m)
    lowest=min(m)
    print(f"\nAverage: {average}\nHighest: {highest}\nLowest: {lowest}")
    print(f"\nPassed: {passcount}\nFailed: {len(m)-passcount}")
    topper=None
    high=0
    for i in range(len(n)):
        if (m[i]>high):
            high=m[i]
            topper=n[i]
    print(f"\nTopper: {topper}")
    return(None)

name,mark=get_inp()
grade=grade_analyser(mark)
calc(name,mark,grade)