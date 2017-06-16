
name=input("enter file name")
file1=open(name, 'r')
sum1=0
count=0
line=file1.readline()
while line!="":
    for str in line.split(","):
        sum1=sum1+eval(str)
        count +=1
    line=file1.readline()

print(" average is", sum1/count)
