import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#x(n)=[1,3,2,4]  h(n)=[2,1,3]

n=np.arange(6)
#时域卷积
x=[1,3,2,4]
h=[2,1,3]
y = signal.convolve(x, h)
wsy, hy = signal.freqz(y,whole= True)
#频域相乘
wsx, hx = signal.freqz(x,whole= True)
wsh, hh = signal.freqz(h,whole= True)
Y = hx * hh
print(abs(hy))
plt.title('时域卷积证明')
plt.figure(1)
plt.plot(wsy, abs(hy), 'b', label='幅度')
plt.grid()
plt.title('时域卷积')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.legend()
plt.twinx()
angles = np.angle(hy)
plt.plot(wsy, angles, 'g', label='相位')
plt.ylabel('角度', color='g')
plt.grid()
plt.legend(loc='lower left')


plt.figure(2)
plt.plot(wsx, abs(Y), 'b', label='幅度')
plt.grid()
plt.title('频域相乘')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.legend()
plt.twinx()
angles = np.angle(Y)
plt.plot(wsx, angles, 'g', label='相位')
plt.ylabel('角度', color='g')
plt.grid()
plt.legend(loc='lower left')

plt.show()