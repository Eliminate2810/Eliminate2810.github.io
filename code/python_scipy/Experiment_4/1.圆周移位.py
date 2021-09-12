import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#x(n)=(2n-1)R_N (n)

def R(n):
    x=np.arange(n)
    x[:]=1
    return x
#周期绘画y（n）
def stemy(n,y,a,b):
    for i in range(a,b):
        const=n+len(n)*i
        plt.stem(const, y, 'b')
    return 0    

a=9
n=np.arange(a+10)
R1=R(a+10)
x=(2*n-1)*R1

y1=np.roll(x,a)
y2=np.roll(x,-a)

#n+9
plt.subplot(211)
plt.title('x(n+9)')

stemy(n,y1,-1,1)
plt.grid()
plt.legend(loc='lower left')
#n-9
plt.subplot(212)
plt.title('x(n-9)')
stemy(n,y2,-1,1)
plt.grid()
plt.legend(loc='lower left')
plt.show()
