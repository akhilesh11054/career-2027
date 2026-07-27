## Exercise 1
names=['John Dutton','Tony Stark','Craig Ferguson','Lewis Hamilton','Lionel Messi']
def fnames(l):
    for n in names:
        l1=n.split()
        print(l1[0])
print('The first names are:')
fnames(names)
def lnames(l):
    for n in names:
        l1=n.split()
        print(l1[1])
print('The lastnames are:')
lnames(names)

print(f'the length of the list :{len(names)}')

## exercise 2
numbers=[10, 25, 30, 45, 50, 65, 70]
for i in range(len(numbers)):
    if(numbers[i]%5==0): print(numbers[i])

## exercise 3
numbers2=list()
def getnumbers():
    n=5
    while n>0:
        inp=int(input("Enter number:"))
        numbers2.append(inp)
        n=n-1
    return(numbers2)
def calc(ls):
    largest=ls[0]
    smallest=ls[0]
    total=0
    for i in ls:
        if(i>largest):largest=i
        if(i<smallest):smallest=i
        total=total+i
    print(f"the list:{ls}")
    print(f"The largest number:,{largest}")
    print(f"The smallest number:{smallest}")
    print(f"The sum:{total}")
numbers2=getnumbers()
calc(numbers2)

##exercise 4
fav_movies=['Godfather','Interstellar','Dune','Shutter Island','KillBill']
def movie_match():
    ls=list()
    u_movie=input('Enter a movie name:')
    for movie in fav_movies:
        if (movie==u_movie):
            ls.append(1)
        else:
            ls.append(0)
    if (max(ls)==1): print("movie found")
    if (max(ls)==0): print("movie not found")
movie_match()