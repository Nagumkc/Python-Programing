import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
meanx=np.mean(x)
meany=np.mean(y)
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
slope=num/den
intercept=meany-(slope*meanx)
print("slope",slope)
print("intercept",intercept)
val=(slope*x)+intercept
plt.plot(x,y)
plt.plot(x,val)
plt.show()