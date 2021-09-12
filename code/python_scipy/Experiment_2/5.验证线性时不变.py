import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

nmin=0
nmax=10
n=np.arange(nmin,nmax+1,1)
n1=len(n)

den=[1.0,0.35,-0.8]
num=[2.5,-1.8,0.0]

x=0.5**n
y0=np.array([0.0,0.0])

x01=np.array([0])
zi1=signal.lfilter_zi(num,den)
y1,_=signal.lfilter(num,den,x,zi=zi1*x01)

x02=np.zeros(n1)
zi2=signal.lfiltic(num,den,y0)
y2,_=signal.lfilter(num,den,x02,zi=zi2)

x2=n/2
y5,_=signal.lfilter(num,den,x2,zi=zi2)

x3=2*0.5**n+2*n
y6,_=signal.lfilter(num,den,x3,zi=zi2)

y3,_=signal.lfilter(num,den,x,zi=zi2)

t4,y4=signal.dimpulse((num,den,1),n=n1)

x4=0.5**(n+2)
y7,_=signal.lfilter(num,den,x4,zi=zi2)

plt.subplot(411)
plt.stem(n,y3)
plt.xlabel('n')
plt.ylabel('(x1=0.5^n)')
plt.ylim(-10,10)

plt.subplot(412)
plt.stem(n,y5)
plt.xlabel('n')
plt.ylabel('(x2=n/2)')
plt.ylim(-10,10)

plt.subplot(413)
plt.stem(n,y6)
plt.xlabel('n')
plt.ylabel('(x3=2*x1+x2)')
plt.ylim(-10,10)

plt.subplot(414)
plt.stem(n,y7)
plt.xlabel('n')
plt.ylabel('(x4=x1(n+2)')
plt.ylim(-10,10)

plt.show()