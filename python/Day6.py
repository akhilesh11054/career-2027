#ex1
inv=list()
def get_info():
    n=int(input('Enter no. of products: '))
    while(n>0):
        product={}
        product['Name']=input('Enter Name of the product: ')
        product['Price']=input('Enter product price: ')
        product['Stock']=int(input('Enter Stock: '))
        inv.append(product)
        n-=1
    return inv
def disp_inv(li):
    for pro in li:
        print()
        print(f"Product name:{pro['Name']}")
        print(f"Price:{pro['Price']}")
        print(f"Stock:{pro['Stock']}\n")
inventory=get_info()
disp_inv(inventory)

