import numpy as np

x = [75,30,83,83,12,49,71,7,72]
y = [62,66,55,34,71,55,58,83,0]
d = 0

for i in range(0,len(x)):
    d += abs(x[i] - y[i])


print(d)