str=input("enter string")
count=0
total=0
for x in range(len(str)):
    if(str[x].isalpha()):
        total += 1
    else:
        count += 1
print("integers count is",count,"characters count is",total)
