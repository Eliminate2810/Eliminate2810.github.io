import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal 
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#x(n)=2cos (a×0.1πn)u(n)+ 2cos (0.4πn)u(n)

fs=10*10e3
wp=0.2*np.pi
ws=0.3*np.pi
Rp=1
As=15


#design digtal butter
N, wc = scipy.signal.buttord(wp/np.pi, ws/np.pi, Rp, As, analog=False, fs=None)
b1, a1 = scipy.signal.butter(N, wc, btype='low', analog= False, output='ba', fs=None)
ws, h = signal.freqz(b1,a1,whole= False)

#generate a signal
a=9
def u(n):
    u = np.where(n >= 0, 1, 0)
    return u
n=np.arange(512)
xn=2*np.cos (a*0.1*np.pi*n)*u(n)+ 2*np.cos (0.4*np.pi*n)*u(n)

zi1 = signal.lfilter_zi(b1, a1)
yn,_ = signal.lfilter(b1, a1, xn, zi=zi1)

#plot fileter
plt.semilogx(ws, abs(h))
plt.title('Butterworth 数字低通滤波器')
plt.xlabel('Frequency [rad]')
plt.ylabel('Amplitude ')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')

#plot x and y
i=np.arange(100)
x=xn[0:100]
y=yn[0:100]
plt.figure(2)
plt.subplot(211)
plt.stem(i,x)
plt.title('x(n) and y(n)')
plt.grid()
plt.subplot(212)
plt.stem(i,y)
plt.grid()
plt.show()