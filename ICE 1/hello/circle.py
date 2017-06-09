#calculate perimeter and area
import math

num1= input("enter radius")
x=int(num1)
area=math.pi * x* x
per= 2* math.pi * x
print("area:",area)
print("perimeter", per)