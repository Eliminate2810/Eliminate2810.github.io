import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def u(n):
    bot=-50; top=50
    a = np.arange(bot, top)
    a[:] = 0
    a[n+bot:] = 1
    return a

#x(n)=(n+1)R_N (n), h(n)=(n-1)[u(n+2)-u(n-N)]
top = 50; bot = -50; a = 9
n = np.arange(bot, top)
x = (n+1) * (u(0) - u(a))
h = (n-1)*(u(-2) - u (a)) 

y = np.arange(bot, top)
y[:]=0
y = signal.convolve(x, h)
plt.axis([-10, 20, -50, 180])
#x范围
xx = np.arange(bot*2, 2*top-1)
plt.stem(xx, y)
plt.show()
