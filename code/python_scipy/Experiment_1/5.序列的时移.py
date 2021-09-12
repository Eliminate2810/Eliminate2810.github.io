import matplotlib.pyplot as plt
import numpy as np
import math as m

#y(n)=x(n-m)，其中x(n)=2n，0≤n≤20,m=9
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title("y(n)=x(n-m)")
#变量
top=21; bot=0
m=9
n = np.arange(bot, top+10)
x = np.arange(-10, top+20)
y = np.arange(bot, top+10)
x[:] = 0 # x初始化
# x赋值
for i in range(bot, top):
    x[i] = 2 * n[i]
y[:] = 0  
# y赋值
for i in range(bot, top):
    y[i] = x[i-m]
    print(y[i])

plt.axis([0, 25, 0, 25])
plt.stem(n, y)
plt.show()
