import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal 
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

wp1=0.2*np.pi
ws1=0.3*np.pi
Rp=1
As=15
wp=np.tan(wp1/2)
ws=np.tan(ws1/2)

#design butterworth with frequen-to-range
N, wc = scipy.signal.buttord(wp, ws, Rp, As, analog=True, fs=None)
b1, a1 = scipy.signal.butter(N, wc, btype='low', analog=True, output='ba', fs=None)
bz,az=signal.bilinear(b1,a1,0.5)
ws, h = signal.freqz(bz,az,whole= False)

plt.semilogx(ws, abs(h))
plt.title('双线性 Butterworth 数字低通滤波器')
plt.xlabel('Frequency [rad]')
plt.ylabel('Amplitude ')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.show()
