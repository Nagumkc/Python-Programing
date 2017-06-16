arr=['hello','world','python','cs']
count=0
str =""
for x in range(len(arr)):
    if(count<len(arr[x])):
        count=len(arr[x])
        str=arr[x]
print(str,count)