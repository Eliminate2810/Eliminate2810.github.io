import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#y+0.1ay-0.25y=x+x+2x

a=9
num = [1.0, 1.0, 2.0]
den = [1.0, 0.1*a, -0.25]
z,p,k = signal.tf2zpk(num,den)

#plot circle
r = 1;
print(r)
theta = np.arange(0, 2*np.pi, 0.01)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure(1)
plt.plot(x, y, 'black', label='单位圆')
plt.axis('equal')
#plot z & p
plt.plot(z, 'o', color='b', label='零点')
plt.plot(p, 'x', color='g', label='极点')
plt.legend(loc='lower left')
plt.grid()
plt.title('零极点图')

#plot 幅频特性
ws, h = signal.freqz(num,den,whole= False)
plt.figure(2)
plt.title('幅频和相频')
plt.plot(ws, abs(h), 'b', label='幅频曲线')
plt.ylabel('幅度')
plt.xlabel('频率')
plt.legend(loc='lower left')
plt.twinx()
angles = np.angle(h)
plt.plot(ws, angles, 'g', label='相频曲线')
plt.ylabel('角度', color='g')
plt.grid()
plt.legend(loc='upper right')
plt.grid(plt.figure(2))

#plot 系统输出
nmin=0
nmax=8
n=np.arange(nmin,nmax+1,1)
n1=len(n)

x=2*np.cos(0.1*a*np.pi*n)
x01 = np.array([0])
zi1 = signal.lfilter_zi(num, den)
y3,_ = signal.lfilter(num, den,x, zi=zi1)

plt.figure(3)
plt.stem(n, y3)
plt.xlabel('n')
plt.ylabel('全响应')
plt.title('系统输出图')
plt.grid(plt.figure(3))

plt.show()
