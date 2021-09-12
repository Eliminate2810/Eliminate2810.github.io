import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

n = np.arange(-5,20)
y = np.arange(-5,20)
y[:]=0
y[5:]=1

plt.axis([-5, 15, 0, 2.0])
plt.stem(n, y)  # 离散序列作图函数
plt.xlabel('Time n')
plt.ylabel('Amplitude')
plt.title('单位阶跃序列：u(n-n0)')
plt.show()
