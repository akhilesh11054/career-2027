n=5
while n>0:
    print("Hello!")
    n=n-1

for i in range(1,11):
    print(i)

for i in range(2,21):
    if(i%2==0): print(i)


n=input("enter a number:")
n=int(n)
for i in range(1,11):
    print(f"n*{i}={n*i}")


while True:
    pw=input("enter password")
    if(pw=='python123'): break
print("Access Granted")