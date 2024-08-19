import random
from colorama import init,Fore,Back

init(convert=True)

computer_guess=random.randint(1,100)
y=0
score=1000
errors=0
Quit=0

print(Back.BLACK+Fore.WHITE+"\nHello my dear firend!",chr(0x2665))
print("your current score is: ",score,"\n")
print(Fore.BLUE + 'Remember that if you want to quit the game anytime, Just press '+Fore.GREEN+ 'Q!')

while score>0:
    user_guess=input(Fore.WHITE+"please enter your guess:")
    list=[]
    for i in user_guess:
        list=list+[i]
    if list==[]:
        print(Fore.CYAN+"you have not entered any data!!\n")
        if errors==0:
            print(Fore.CYAN+"if you enter a wrong or empty input once more, you'll lose score!\n ")
            errors=errors+1
        else:
            score=score-100
            print(Fore.WHITE+"your current score is: ",score,"\n")
        continue
    else:
        x=0
        for i in list:
            if len(list)==1 and i=="Q":
                Quit=1
                
            elif ord(i)>=58 or ord(i)<=47:
                print(Fore.CYAN+"out of context!")
                if errors==0:
                    print(Fore.CYAN+"if you enter a wrong input once more, you'll lose score!\n ")
                    errors=errors+1
                else:
                    score=score-100
                    print(Fore.WHITE+"your current score is: ",score,"\n")
                x=x+1
                break
            
        if Quit==1:
            break
        
        elif x!=0:
            continue
        
        elif x==0:
            user=int(user_guess)
            if (user)>100 or (user)<0:
                print(Fore.CYAN+"out of range. try again!\n")
                if errors==0:
                    print(Fore.CYAN+"if you enter a wrong input once more, you'll lose score!\n ")
                    errors=errors+1
                else:
                    score=score-100
                    print(Fore.WHITE+"your current score is: ",score,"\n")
            elif (user)>computer_guess:
                print(Fore.YELLOW+"your guess is high!")
                score=score-100
                print(Fore.WHITE+"your current score is: ",score,"\n")
            elif (user)<computer_guess:
                print(Fore.YELLOW+"your guess is low!")
                score=score-100
                print(Fore.WHITE+"your current score is: ",score,"\n")
            else:
                print(Fore.GREEN+"you made it! :)")
                print(Fore.GREEN+"your Final score is: ",score,"\n")
                y=1
                break
if y!=1 and Quit==0:
    print(Back.RED+"Game Over")
    print(Fore.WHITE+"you lost all your scores! :(")
elif y!=1 and Quit!=0:
    print(Fore.MAGENTA+"See you later dude!",chr(0x2665),"\n" )