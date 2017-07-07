li=[{'course':"python",'lastgpa':90,'currentgpa':80},{'course':"python",'lastgpa':95,'currentgpa':85},{'course':"python",'lastgpa':100,'currentgpa':100}]
for i in range(0,len(li)):
    a=li[i]['lastgpa']
    b=li[i]['currentgpa']
    c=(a+b)/2;
    del li[i]['lastgpa']
    del li[i]['currentgpa']
    li[i]['lastgpa+currentgpa']=c
    a=0
    b=0
print(li)