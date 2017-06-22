str=input("enter string")
dic={}
for i in range(len(str)):
    dic[str[i]]=str.count(str[i])+1
if(len(dic)==26):
    print("it contains all letters")
else:
    print("not found all letters")
