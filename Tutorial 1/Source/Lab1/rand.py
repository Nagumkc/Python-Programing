from random import randint
rnum=randint(0,9)
num1=input("Guess the digit")
x=int(num1)
print("random number generated is "+str(rnum))
if(x==rnum):
    print("your guessing is right!")
else:
    if(x>rnum):
        print("your answer is higher than expected")

    else:
        print("your answer is lower than expected")
