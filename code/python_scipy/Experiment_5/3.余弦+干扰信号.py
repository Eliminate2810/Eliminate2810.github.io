import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#generate a signal
a=9
f=20*10**6 #20Mhz
T=1.0/f
fs=100*10**6 #100Mhz
na=np.linspace(0,a*T,int(a*T*fs))
xn=2*np.cos(2*np.pi*f*na)
yn=np.random.rand(len(na))
xn0=xn+yn

#xn,Xk
#FFT changez`
plt.figure(1)
Xk=np.fft.fft(xn0)
freq = np.fft.fftfreq(len(xn0),d=1/(fs))
plt.subplot(211)
plt.title('x(n)')
plt.stem(na,xn0) 
plt.subplot(212)
plt.title('X(k)')  
plt.plot(freq,abs(Xk))
#yn,Yk
#FFT change
plt.figure(2)
Yk=np.fft.fft(yn)
freq = np.fft.fftfreq(len(yn),d=1/(fs))
plt.subplot(211)
plt.title('y(n)')
plt.stem(na,yn) 
plt.subplot(212)
plt.title('Y(k)')  
plt.plot(freq,abs(Yk))
plt.show()