import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.fftpack import fft,fftshift
from scipy import signal 
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


window = signal.triang(51)
plt.plot(window)
plt.title("Triangular window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.figure()
A = fft(window, 2048)/ (len(window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
print(fftshift(A /abs(A).max()))
response = 20 * np.log10(np.abs(fftshift(abs(A) /abs(A).max())))
plt.plot(freq, response)
plt.axis([-0.5,0.5,-120,0])
plt.title("Frequency response of the triangular window")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
