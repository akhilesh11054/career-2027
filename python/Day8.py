#----Scratch#1(printusingwhileloop)-----
# fruit='banana'
# i=0
# while(i<len(fruit)):
#     letter=fruit[i]
#     print(letter)
#     i+=1

#----Scratch#2(backwordloop)----
# fruit='banana'
# i=len(fruit)-1
# while(i>=0):
#     letter=fruit[i]
#     print(letter)
#     i-=1

#----scratch3(slicing+concatenating)----
# name1='lance'
# name2='harry'
# new_name=name1[:2]+name2[2:]
# print(new_name)

# ---scratch4(counting letter)-----
# def count_let(word):
#     count=0
#     for ch in word:
#         if(ch=='a'or ch=='A'):count+=1
#     print(count)
# fruit='bananaaaa'
# count_let(fruit)

#----Scratch(random)----
# word='banana'
# new_word=word.upper()
# print(new_word)
# print(new_word.capitalize())
# print(word.startswith('b'))

# #---Scratch(parsing_strngs)----
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# at_pos=data.find('@')
# s_pos=data.find(' ',21)
# address=data[at_pos+1:s_pos]
# print('address:',address)

#----py4eExc---
str = 'X-DSPAM-Confidence: 0.8475'
hy_pos=str.find(':')
val=str[hy_pos+1:]
value=float(val)
print(value)
