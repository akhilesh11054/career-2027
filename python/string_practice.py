# #exc1
# word='elephant'
# index=0
# while (index<len(word)):
#     print(word[index])
#     index+=1

# #exc2
# word=input('enter a word:')
# vowelcount=0
# for ch in word:
#     if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
#         vowelcount+=1
# print(vowelcount)

# #exc3
# word=input('Enter a word:')
# uppercase=0
# lowercase=0
# for ch in word:
#     if (ch.isupper()):
#         uppercase+=1
#     elif(ch.islower()):
#         lowercase+=1
# print(f"Uppercase:{uppercase}\nLowercase:{lowercase}")

# #exc4
# word=input('enter a word:')
# index=len(word)-1
# rword=''
# while (index>=0):
#     rword=f"{rword}{word[index]}"
#     index-=1
# print(rword)

# # exc5
# word=input("enter a word: ")
# letter=input("enter search letter: ")
# count=0
# for ch in word:
#     if(ch==letter): count+=1
# print(count)

# #exc6
# word=input('enter a word: ')
# palindrome=None
# for i in range(len(word)):
#     if(word[i]==word[len(word)-i-1]):
#         palindrome=True
#         continue
#     else: 
#         palindrome=False
#         print('Not Palindrome')
#         break
# if(palindrome==True):
#     print('Palindrome')
# elif(palindrome==None):
#     print('Invalid Entry')

# #exc7
# sen=input('enter input sentence:')
# n_sen=''
# for ch in sen:
#     if(ch!=' '):
#         n_sen=f"{n_sen}{ch}"
# print(n_sen)

#exc8
pw=input('enter new password:')
length=None
ucase=None
lcase=None
digi=None
if(len(pw)>=8):
    length=True
else:
    length=False

u_count=0
l_count=0
digi_count=0
for ch in pw:
    if(ch.isupper()):
        u_count+=1
    if(ch.islower()):
        l_count+=1
    if(ch.isdigit()):
        digi_count+=1
if (u_count>=1): ucase=True
else: ucase=False
if (l_count>=1): lcase=True
else: lcase=False    
if(digi_count>=1): digi=True
else: digi=False

if length and ucase and lcase and digi:
    print("Valid password")
else:
    print('invalid password')


