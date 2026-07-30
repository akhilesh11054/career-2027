def get_info():
    contacts=dict()
    n=5
    while n>0:
        name=input('enter name: ')
        contacts[name]={}
        contacts[name]['phone']=input('Enter phone:')
        contacts[name]['email']=input('enter email: ')
        n-=1
    return contacts
def cont_disp(d1):
    print('\n\n----CONTACTS----')
    for d in d1:
        print(f"{d} - {d1[d]['phone']} - {d1[d]['email']}")

def cont_search(d):
    ser=input('\nenter name to search: ')
    try:
        print(f"\nPhone:{d[ser]['phone']}\nEmail:{d[ser]['email']}")
    except:
        print('user not found')


cont=get_info()
cont_disp(cont)
cont_search(cont)

