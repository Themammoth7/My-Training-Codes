import string
import random
from colorama import init,Fore,Back
init(convert=True)


Lowercase=string.ascii_lowercase
Uppercase=string.ascii_uppercase
Digits=string.digits
punctuations=string.punctuation
allinone=Lowercase+Uppercase+Digits+punctuations


length=int(input(Fore.WHITE+"How many characters would you like your password has?: "))

print("Enter a number with special digits for each kind of constant that your password must have:")
print(Fore.BLUE+" 1 for Digits\n 2 for Lowercase letters\n 3 for Capital letters\n 4 for punctuations and special letters")


req=input(Fore.WHITE+"enter a number based on your ideal password:")

error=0
while error==0:

#cleaning what the user really wants. remove non-numeric values and repeated ones
    req1=[]
    for i in req:
        if (i in req1) or (ord(i)>=53 or ord(i)<=48):
            continue
        else:
            req1=req1+[i]
    if len(req1)>length:
        error=0
        req=input(Fore.RED+"enter a number based on your ideal password Again:")
    else:
        break

#it would recommend you a password even if you don't give it any clue

password=''
for i in req1:
    if int(i)==1:
        password=password+Digits[random.randrange(10)]
    elif int(i)==2:
        password=password+Lowercase[random.randrange(26)]
    elif int(i)==3:
        password=password+Uppercase[random.randrange(26)]
    elif int(i)==4:
        password=password+punctuations[random.randrange(32)]

i=length-len(password)
if len(password)<length:
    while i>0:
        password=password+allinone[random.randrange(94)]
        i=i-1

passw = list(password)  
random.shuffle(passw)  
password1 = ''.join(passw)     
print(password1)



