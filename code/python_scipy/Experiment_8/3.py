import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.fftpack import fft,fftshift
from scipy import signal 
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

wp = 0.3 * np.pi
ws = 0.5 * np.pi
rp=0.1
rs=50
num=99
wc=0.5*(wp+ws)

window = np.hamming(num)
N=6.6*np.pi/(ws-wp)     
tao=(N-1)/2
n=np.arange(num)
hd=np.sin(wc*(n-tao)) / (np.pi*(n-tao))
h=window*hd
h[int(tao)]=wc/np.pi
hhh=h[0:34]

plt.subplot(211)
plt.plot(hhh)
plt.title("hamming window h filter")

A = fft(hhh, 2048)/ (len(hhh)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
print(fftshift(A /abs(A).max()))
response = 20 * np.log10(np.abs(fftshift(A /abs(A).max())))
plt.subplot(212)
plt.plot(freq, response)
plt.show()