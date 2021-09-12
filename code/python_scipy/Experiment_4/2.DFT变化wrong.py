import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#mydft(xn,N)   xn=2cos(3n)
nmax=35

def mydft(xn,N):
    Xk=np.arange(nmax, dtype=complex)
    Xk[:]=0.0
    if N<=len(xn):
        for k in range(0, N):
            for i in range(0,N):
                Xk[k]=Xk[k]+xn[i]*(np.cos(np.pi*i*k/N*2)+1j*np.sin(np.pi*i*k/N*2))
    return Xk            
    return 0

n=np.arange(nmax)
x=2*np.cos(1/8*np.pi*n)
y=mydft(x, 13)
print(y)
ws, h = signal.freqz(y,whole=True)

plt.figure(1)
plt.title('x=2cos（1/8*π*n）')
plt.stem(n,x)

plt.figure(2)
plt.title('幅频特性')
plt.plot(ws, abs(h), 'b', label='幅频曲线')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.legend(loc='lower left')
plt.show()