import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.fftpack import fft,fftshift
from scipy import signal 
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#figure 1
window1 = signal.triang(99)
plt.subplot(241)
plt.plot(window1)
plt.title("Triangular window")

A = fft(window1, 2048)/ (len(window1)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
print(fftshift(A /abs(A).max()))
response = 20 * np.log10(np.abs(fftshift(A /abs(A).max())))
plt.subplot(245)
plt.plot(freq, response)

#figure 2
window2 = np.hanning(99)
plt.subplot(242)
plt.plot(window2)
plt.title("hanning window")

A = fft(window2, 2048)/ (len(window2)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
print(fftshift(A /abs(A).max()))
response = 20 * np.log10(np.abs(fftshift(A /abs(A).max())))
plt.subplot(246)
plt.plot(freq, response)

#figure 2
window3 = np.hamming(99)
plt.subplot(243)
plt.plot(window3)
plt.title("hamming window")

A = fft(window3, 2048)/ (len(window3)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
print(fftshift(A /abs(A).max()))
response = 20 * np.log10(np.abs(fftshift(A /abs(A).max())))
plt.subplot(247)
plt.plot(freq, response)

#figure 4
window4 = np.blackman(99)
plt.subplot(244)
plt.plot(window4)
plt.title("blackman window")

A = fft(window4, 2048)/ (len(window4)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
print(fftshift(A /abs(A).max()))
response = 20 * np.log10(np.abs(fftshift(A /abs(A).max())))
plt.subplot(248)
plt.plot(freq, response)
plt.show()
