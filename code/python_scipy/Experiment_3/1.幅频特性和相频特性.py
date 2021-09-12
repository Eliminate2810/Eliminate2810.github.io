import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#y(n)-0.1∙a∙y(n-1)=x(n)+2x(n-1)

nmin=0
nmax=512
n=np.arange(nmin,nmax,1)
n1=len(n)
a=9
den=[1.0,-0.1*a]
num=[1.0,2.0]

ws, h = signal.freqz(num,den,whole= False)

plt.figure(1)
plt.title('Digital frequency response(false)')
plt.plot(ws, abs(h), 'b', label='幅频曲线')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.legend(loc='lower left')
plt.twinx()

angles = np.angle(h)
plt.plot(ws, angles, 'g', label='相频曲线')
plt.ylabel('角度', color='g')
plt.grid()
plt.legend()

#chart 2
ws, h = signal.freqz(num,den,whole= True)

plt.figure(2)
plt.title('Digital frequency response(true)')
plt.plot(ws, abs(h), 'b', label='幅频曲线')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.legend(loc='lower left')
plt.twinx()

angles = np.angle(h)
plt.plot(ws, angles, 'g', label='相频曲线')
plt.ylabel('角度', color='g')
plt.grid()
plt.legend()
plt.show()

