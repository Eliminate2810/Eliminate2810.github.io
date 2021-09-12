import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

nmin=0
nmax=8
n=np.arange(nmin,nmax+1,1)
n1=len(n)

num = [1,-0.9]
den = [1,0]

x=n==0
y0=np.array([1.0,0.0])

t4,y4=signal.dimpulse((num,den,1),n=n1)

zi2=signal.lfiltic(num,den,y0)
y3,_=signal.lfilter(num,den,x,zi=zi2)

tout,yout = signal.dstep ((num, den,1),n=n1)

plt.subplot(311)
plt.stem(n,y3)
plt.xlabel('n')
plt.ylabel('单位冲激响应(lfilter)')
plt.ylim(-2,2)

plt.subplot(312)
plt.stem(t4,np.squeeze(y4))
plt.xlabel('n')
plt.ylabel('单位冲激响应(dimpulse)')
plt.ylim(-2,2)

plt.subplot(313)
plt.stem(tout,np.squeeze(yout))
plt.xlabel('n')
plt.ylabel('单位阶跃响应(destep)')
plt.ylim(-2,2)

plt.show()
