import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#y(n)-0.6y(n-1)=x(n)+2x(n-1)，初始条件为y(-1)=1，求输入为x(n)=(0.1∙〖a)〗^n u(n)时系统的零状态、零输入、全响应


nmin=0
nmax=8
n=np.arange(nmin,nmax+1,1)
n1=len(n)

num = [1,-0.6]
den = [1,2]

x=(0.1*9)**n
y0=np.array([1.0,5/3])

x01=np.array([0])
zi1=signal.lfilter_zi(num,den)
y1,_=signal.lfilter(num,den,x,zi=zi1*x01)

x02=np.zeros(n1)
zi2=signal.lfiltic(num,den,y0)
y2,_=signal.lfilter(num,den,x02,zi=zi2)

y3,_=signal.lfilter(num,den,x,zi=zi2)

t4,y4=signal.dimpulse((num,den,1),n=n1)

plt.subplot(411)
plt.stem(n,y1)
plt.xlabel('n')
plt.ylabel('零状态响应')
plt.ylim(-50,300)

plt.subplot(412)
plt.stem(n,y2)
plt.xlabel('n')
plt.ylabel('零输入响应')
plt.ylim(-50,300)

plt.subplot(413)
plt.stem(n,y3)
plt.xlabel('n')
plt.ylabel('全响应')
plt.ylim(-50,300)

plt.subplot(414)
plt.stem(t4,np.squeeze(y4))
plt.xlabel('n')
plt.ylabel('单位冲激响应')
plt.ylim(-50,500)

plt.show()
