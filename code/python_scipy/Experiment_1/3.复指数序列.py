import matplotlib.pyplot as plt
import numpy as np
import math

#e^(c+jw)n
c = 0.2; w = 0.3

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# Create a new subplot from a grid of 2x1
plt.subplot(2, 1, 1)
plt.title("复指数序列实部和虚部")
#图幅变量
x1 = -5;x2 = 30;y1 = 0;y2 = 180


#                                   p1
#变量
n = np.arange(-1,26)
y = np.arange(-1,26) #初始化y
#y赋值
for i in range(-1, 26):
    y[i+1] = math.exp(n[i]*c)

plt.stem(n, y, label='实部')
#setting table
plt.xlim(x1, x2)
plt.xticks(np.linspace(x1, x2, 7, endpoint=True))
plt.ylim(y1, y2)
plt.yticks(np.linspace(y1, y2, 5, endpoint=True))
plt.legend(loc='lower left')


#                                       p2
plt.subplot(2, 1, 2)
#变量
n = np.arange(-1,26)
y = np.arange(-1,26) #初始化y
#y赋值
for i in range(-1, 26):
    y[i+1] = math.exp(n[i]*w)
    print(y[i])

plt.stem(n, y, label='虚部')
#setting table
plt.xlim(x1, x2)
plt.xticks(np.linspace(x1, x2, 7, endpoint=True))
plt.ylim(y1, y2)
plt.yticks(np.linspace(y1, 2000, 5, endpoint=True))
plt.legend(loc='lower left')

plt.show()
