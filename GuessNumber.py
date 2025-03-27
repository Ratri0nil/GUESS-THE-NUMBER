import random

randnum = random.randint(0,100)

while True:

    userchoice=input("enter the number you guess or quit(Q): ")
    if(userchoice=="Q" or userchoice=="q"):
        break
    else:
        usernum=int(userchoice)

    if(usernum==randnum):
        print("yay ! you won")
        break
    elif(usernum>randnum):
        print("oh no ! too big guess")
    else:
        print("oh no ! too small guess")



print("Thanks for playing.")





