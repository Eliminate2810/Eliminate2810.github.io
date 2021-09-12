import matplotlib.pyplot as plt
import numpy as np
import math as m

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title("3190432099")
#变量
top=216
bot=0
n = np.arange(bot, top)
y = np.arange(bot, top)
#y赋值
for i in range(bot, top):
    y[i] = 2*m.cos(0.25*m.pi*n[i]) + 3*m.sin(0.3*m.pi*n[i])

plt.stem(n, y)
plt.show()
