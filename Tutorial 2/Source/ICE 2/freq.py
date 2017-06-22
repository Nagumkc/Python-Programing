str=input("enter string")
dict={}
for x in range(len(str)):
 dict[str[x]]=str.count(str[x])
print(dict)

