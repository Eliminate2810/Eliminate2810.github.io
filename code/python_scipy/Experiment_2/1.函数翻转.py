import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#x(n)=(2n-1)[u(n+3)-u(n-a)]
def u(n):
    bot=-20; top=20
    a = np.arange(bot, top)
    a[:] = 0
    a[n+bot:] = 1
    return a

top = 20; bot = -20; a = 9
n1 = np.arange(bot, top)
#calculate
x = (2*n1-1)*(u(-3)-u(a))
#before and after
x = np.flipud(x)

plt.axis([bot, top, -10, 20])
plt.stem(n1, x)
plt.show()