import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#x1(n)=R_a (n)，x2(n)=R_b (n) ，x3(n)=R_c (n)

a=9
x1=np.arange(a)
x1[:]=1
x2=np.arange(a+20)
x2[:]=1
x3=np.arange(a+40)
x3[:]=1

ws, h = signal.freqz(x1,whole=True)
plt.subplot(311)
plt.title('幅频特性')
plt.plot(ws, abs(h), 'b', label='R_9 (n)')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.grid()
plt.legend(loc='lower left')

ws, h = signal.freqz(x2,whole=True)
plt.subplot(312)
plt.plot(ws, abs(h), 'b', label='R_29 (n)')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.grid()
plt.legend(loc='lower left')

ws, h = signal.freqz(x3,whole=True)
plt.subplot(313)
plt.plot(ws, abs(h), 'b', label='R_49 (n)')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.grid()
plt.legend(loc='lower left')
plt.show()