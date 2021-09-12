import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal 


fp=99
fs=250
Rp=2.5
As=47
wp=np.pi*2*fp
ws=np.pi*2*fs

#design butterworth with frequen-to-range
N, wc = scipy.signal.buttord(wp, ws, Rp, As, analog=True, fs=None)
b1, a1 = scipy.signal.butter(N, wc, btype='low', analog= True, output='ba', fs=None)
w1,h1 = scipy.signal.freqs(b1, a1)
#prototype
z, p, k = scipy.signal.besselap(N, norm='phase')
b2, a2 = scipy.signal.zpk2tf(z, p, k)
w2,h2 = scipy.signal.freqs(b2, a2)

plt.subplot(211)
plt.semilogx(w1, 20 * np.log10(abs(h1)))
plt.title('Butterworth filter frequency response and lowpass prototype')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(620, color='blue') 

plt.subplot(212)
plt.semilogx(w2, 20 * np.log10(abs(h2)))
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(1, color='blue') 

plt.show()
