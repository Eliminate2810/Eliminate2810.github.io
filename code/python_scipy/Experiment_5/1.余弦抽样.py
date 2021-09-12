import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#generate a signal
a=9
f=99*10**6 #99Mhz
T=1.0/f
fs=990*10**6 #990Mhz
na=np.linspace(0,a*T,int(a*T*fs))
xn=np.cos(2*np.pi*f*na)

#FFT change
Xk=np.fft.fft(xn)
freq = np.fft.fftfreq(len(xn),d=1/(fs))
plt.subplot(211)
plt.title('x(n)')
plt.stem(na,xn) 
plt.subplot(212)
plt.title('X(k)')  
plt.stem(freq,Xk)
print(Xk)
plt.show()