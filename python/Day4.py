#def comp_pay(hours,rate):
#    if(hours>8):
#        pay=8*rate+((hours-8)*(rate*1.5))
#    else:
#        pay=hours*rate
#    return pay
#x=comp_pay(2,10)
#print(x)


#def print_name(name):
#    print(name)
#nam="akhilesh"
#print_name(nam)


#def greeting():
#    name=input("Enter your name:")
#    print(f"Hello,{name}")
#greeting()


#def greet(name):
#    print(f"hello,{name}")
#greet("akhilesh")


#def add_two(x,y):
#    sm=x+y
#    return sm
#a=add_two(2,4)
#print(a)


#def oddeven(x):
#    if(x%2==0):
#        print(f'{x} is even')
#    else:
#        print(f'{x} is odd')
#oddeven(4)


def factorial(x):
    fact=1
    while(x>0):
        fact=fact*x
        x=x-1
    print(fact)
factorial(10)
