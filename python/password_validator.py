
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
