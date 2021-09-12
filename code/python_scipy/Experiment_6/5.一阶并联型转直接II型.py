import matplotlib.pyplot as plt
from scipy import signal

k=9
r=[1,2,3]
p=[0.6,0.7,0.8]
b,a = signal.invresz(r,p,k)
print(b,"\n",a)