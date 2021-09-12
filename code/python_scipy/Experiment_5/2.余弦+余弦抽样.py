import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def cos(fs,n):
    return np.cos(2*np.pi*fs*n)

#generate signal
a=9
f1=a*10*10**6
f2=20*10**6
T=1/(10*10**6)
fs=180*10**6
t=linspace(0,a*T,int(a*T*fs))
x1=cos(f1,t)
x2=cos(f2,t)
xn=x1+x2

#FFT change
Xk=np.fft.fft(xn)
freq = np.fft.fftfreq(len(xn),d=1/(fs))
plt.subplot(211)
plt.title('x(n)')
plt.stem(t,xn) 
plt.subplot(212)
plt.title('X(k)')  
plt.plot(freq,abs(Xk))
plt.show()