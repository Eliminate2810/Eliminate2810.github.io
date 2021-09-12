import matplotlib.pyplot as plt
from scipy import signal

c=99
b=[c,-5.4,-2.74,1.344]
a=[1,-0.5,-0.62,0.336]
r,p,k = signal.residuez(b,a)
print(r)
print(p)
print(k)