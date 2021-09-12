import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#y(x)=x^3+〖ax〗^2+3x-40

a=9
p = np.poly1d([1, a, 3, -40])
answer = np.roots(p)
print(answer)
print(p(a))