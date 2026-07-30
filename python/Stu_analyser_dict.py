def grade_calc(n):
    if (n>90): grade='A+'
    elif(n>80): grade='A'
    elif(n>70): grade='B'
    elif(n>60): grade='C'
    elif(n>50): grade='D'
    elif(n>=40): grade='E'
    else: grade='F'
    return grade 

def topper_calc(da):
    top=0
    for i in da:
        if(i['Mark']>top):
            top=i['Mark']
            topper=i['Name']
    return topper

def get_info():
    db=list()
    n=5
    while(n>0):
        student={}
        student['Name']=input('enter name: ')
        student['Mark']=int(input('enter mark: '))
        student['Grade']=grade_calc(student['Mark'])
        if(student['Grade']=='F'):student['Result']='Fail'
        else:student['Result']='Pass'
        db.append(student)
        n-=1
    return db

def calc(d):
    marks=list()
    failcount=0
    for l in d:
        print(f"{l['Name']} - {l['Mark']} - {l['Grade']}")
        marks.append(l['Mark'])
        if(l['Result']=='Fail'):
            failcount+=1
    print(f'\nAverage: {sum(marks)/len(marks)}')
    print(f'Highest:{max(marks)}')
    print(f"Lowest: {min(marks)}")
    print(f"\nPassed: {len(d)-failcount}")
    print(f"Failed: {failcount}\n")
    print(f"Topper: {topper_calc(d)}")

data=get_info()
calc(data)