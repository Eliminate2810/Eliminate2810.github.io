import matplotlib.pyplot as plt
import numpy as np

#x(n),x(n+3),x(-n-3)
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#变量
top = 20; bot = -20
x1=-2;x2=0;x3=4;x4=8
n = np.arange(bot, top)
x=np.arange(bot, top)
y = np.arange(bot, top)
# y函数
y[:] = 0
for i in range(bot, top):
    if (i>=x1) and (i<x2):
        y[i-bot] = -4-2*i
    elif (i>=x2) and (i<x3):
        y[i-bot] = -4+3*i
    elif (i>=x3) and (i<=x4):
        y[i-bot] = 16-2*i
    else:
        y[i-bot] = 0
#   table1
plt.subplot(3,1,1)
plt.stem(x, y, label="x(n)")
plt.legend(loc='lower left')
#   table2
plt.subplot(3,1,2)
plt.stem(x+3, y, label="x(n+3)")
plt.legend(loc='lower left')
#   table3
plt.subplot(3,1,3)
plt.stem(-1*x-3, y, label="x(-n-3)")
plt.legend(loc='lower left')
plt.show()