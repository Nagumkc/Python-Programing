# reversing a number
num=input(" enter number")
x=int(num)
res=0
while(x>0):
    y=x%10
    res=res*10+y
    x=x//10
print(res)
